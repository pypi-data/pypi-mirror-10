import sys
if not sys.version_info.major < 3:
    print("Sorry, Python 3 is not supported (yet)")
    sys.exit(1)

from setuptools import setup, find_packages

setup(
    name = "sdam",
    version = "0.4",
    packages = ['sdam'],
    entry_points = {
        'console_scripts': ['sdam = sdam:sdam.main'],
    },
    zip_safe = False,
    install_requires = ['twisted>=15.0'],
    author = "Oleksandr Kozachuk",
    author_email = "ddeus.lp@mailnull.com",
    description = "(s)tart programs (d)aemonized (a)nd (m)onitored.",
    license = "WTFPL",
    url = "http://launchpad.net/sdam",
    keywords = "daemon monitoring service",
)
