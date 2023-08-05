#!/usr/bin/python

"""With sdam.py you can start services daemonized and monitored, what
means that they will be restarted automatically and their output will
be put in syslog or a logfile. The command given should run in
foreground and give all output to stdout respective stderr. If sdam.py
is not started daemonized and no logfile is given, than sdam.py will
write the log to stderr.

"""

import sys, os, signal, re, traceback, errno, time

try: import twisted
except:
    sys.stderr.write("No twisted found, please install it with: pip install twisted\n")
    sys.exit(1)

from twisted.application import app, service
from twisted.python import log, syslog, logfile, usage
from twisted.python.util import untilConcludes
from twisted.internet import reactor, protocol
from twisted.internet.interfaces import IReactorDaemonize

BASE_NAME = os.path.basename(sys.argv[0])
APP_NAME = "SDAM"
try:
    import pkg_resources
    VERSION = pkg_resources.require(APP_NAME)[0].version
except: VERSION = '0.0'


class App(protocol.ProcessProtocol):
    def __init__(self, config):
        self.config = config
        self.out = [[], []]

    def connectionMade(self):
        log.msg('Process started with pid %d' % self.transport.pid)
        self.transport.closeStdin()

    def _log(self, data, num, logf):
        self.out[num].append(data)
        if '\n' in data:
            msgs = ''.join(self.out[num]).split('\n')
            if data[-1] != '\n':
                self.out[num] = [msgs[-1]]
            else: self.out[num] = []
            for x in msgs[:-1]:
                if len(x) > 0:
                    logf(x)

    def outReceived(self, data): self._log(data, 0, log.msg)
    def errReceived(self, data): self._log(data, 1, lambda x: log.msg('ERR: ' + x))

    def outConnectionLost(self): self._log('\n', 0, log.msg)
    def errConnectionLost(self): self._log('\n', 1, lambda x: log.msg('ERR: ' + x))

    def processEnded(self, reason):
        log.msg("Process ended with status %d, restart." % reason.value.exitCode)
        reactor.spawnProcess(App(self.config), self.config.rest[0], self.config.rest)
        time.sleep(1)

class AppOptions(usage.Options):
    synopsis = "Usage: %s [options]" % BASE_NAME

    optFlags = [['nodaemon', 'D', "Don't daemonize."],
                ['syslog', None, "Log to syslog, not to file."]]

    optParameters = [['logfile', 'l', None, "Log file name."],
                     ['prefix', None, APP_NAME, "Use the given prefix when syslogging."],
                     ['pidfile','', None, "Name of the pidfile."]]

    compData = usage.Completions(
        optActions={'logfile': usage.CompleteFiles("*.log"),
                    'pidfile': usage.CompleteFiles("*.pid"),
                    'prefix': usage.Completer(descr="syslog prefix")})

    def opt_version(self):
        """
        Display version and exit.
        """
        print("%s %s" % (APP_NAME, VERSION))
        sys.exit(0)

class AppLogger(object):
    def __init__(self, config):
        self.config = config
        self.logfile = config.get('logfile', '')
        self.observer = None

    def start(self):
        if self.config['syslog']:
            self.observer = syslog.SyslogObserver(self.config.get("prefix", "")).emit
        else:
            if self.config['nodaemon'] and not self.logfile:
                logFile = sys.stderr
            else:
                logFile = logfile.LogFile.fromFullPath(self.logfile)
                signal.signal(signal.SIGUSR1, lambda s, f: reactor.callFromThread(logFile.rotate))
            self.observer = log.FileLogObserver(logFile).emit
        log.startLoggingWithObserver(self.observer)
        log.msg("Service %s starting up." % APP_NAME)

    def stop(self):
        log.msg("Service %s shut down." % APP_NAME)
        if self.observer is not None:
            log.removeObserver(self.observer)
            self.observer = None

class AppRunner(object):
    def __init__(self, config):
        self.config = config
        self.logger = AppLogger(config)

    def run(self):
        checkPID(self.config['pidfile'])
        oldstderr = sys.stderr
        if not self.config['nodaemon']:
            self.daemonize()
        if self.config['pidfile']:
            f = open(self.config['pidfile'], 'wb')
            f.write(str(os.getpid()))
            f.close()
        self.logger.start()

        log.msg('Spawn command: %s' % repr(self.config.rest))
        reactor.spawnProcess(App(self.config), self.config.rest[0], self.config.rest)

        try: reactor.run()
        except:
            if self.config['nodaemon']: file = oldstderr
            else: file = open("CRASH.log",'a')
            traceback.print_exc(file = file)
            file.flush()        
        if self.config['pidfile']:
            try: os.unlink(self.config['pidfile'])
            except OSError as e:
                if e.errno == errno.EACCES or e.errno == errno.EPERM:
                    log.msg("Warning: No permission to delete pid file")
                else: log.err(e, "Failed to unlink PID file:")
            except: log.err(None, "Failed to unlink PID file:")
        self.logger.stop()

    def daemonize(self):
        if IReactorDaemonize.providedBy(reactor):
            reactor.beforeDaemonize()
        if os.fork(): os._exit(0)
        os.setsid()
        if os.fork(): os._exit(0)
        null = os.open('/dev/null', os.O_RDWR)
        for i in range(3):
            try: os.dup2(null, i)
            except OSError as e:
                if e.errno != errno.EBADF:
                    raise
        os.close(null)
        if IReactorDaemonize.providedBy(reactor):
            reactor.afterDaemonize()

def checkPID(pidfile):
    if not pidfile: return
    if os.path.exists(pidfile):
        try: pid = int(open(pidfile).read())
        except ValueError: sys.exit('Pidfile %s contains non-numeric value' % pidfile)
        try: os.kill(pid, 0)
        except OSError as why:
            if why[0] == errno.ESRCH:
                log.msg('Removing stale pidfile %s' % pidfile, isError=True)
                os.remove(pidfile)
            else: sys.exit("Can't check status of PID %s from pidfile %s: %s" % (pid, pidfile, why[1]))
        else: sys.exit("""\
Another server is running, PID %s\n
This could either be a previously started instance of your application or a
different application entirely. To start a new one, either run it in some other
directory, or use the --pidfile and --logfile parameters to avoid clashes.
""" %  pid)

def main():
    config = AppOptions()
    args = []; rest = None
    for a in sys.argv[1:]:
        if rest != None: rest.append(a)
        elif a == '--': rest = []
        else: args.append(a)
    if rest is None:
        print(config.__str__())
        print("""To start a service with sdam.py, please specify the command to start after --:

        $> sdam.py -- sleep 10

In this example, the command "sleep 10" will be started and monitored.""")
        sys.exit(1)
    try:
        config.parseOptions(args)
        config.rest = rest
    except usage.error as ue:
        print(config)
        print("%s: %s" % (APP_NAME, ue))        
    else: AppRunner(config).run()
    return 0

if __name__ == '__main__':
    sys.exit(main())
