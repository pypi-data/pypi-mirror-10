======================================================
SDAM - (s)tart programs (d)aemonized (a)nd (m)onitored
======================================================

With sdam you can start services daemonized and monitored, what means
that they will be restarted automatically and their output will be put
in syslog or a logfile. The command given should run in foreground and
give all output to stdout respective stderr. If sdam is not started
daemonized and no logfile is given, than sdam will write the log to
stderr.

To get more help, try:

   $> sdam --help

For now no Python 3 support, because of Twisted, which not supports
Python 3 either.
