flags
=====

*flags* is a Python flag parsing library for humans, not robots.

Why?
****

Argparse is complicated. `Plac <http://plac.googlecode.com/hg/doc/plac.html>`_ remedies most of its issues. However, sometimes you just need a really simple POSIX-style flag parser. You can use getopt, but it makes you write all the help screens yourself, which can easily go out-of-sync with the program source. *flags* aims at filling this void by providing a simple, practical API that's truly easy to use and doesn't suck.

Example
*******

Since README examples always go out of sync with the source, included at ``examples/grep.py`` is *flags* parser for `POSIX grep <http://pubs.opengroup.org/onlinepubs/9699919799/utilities/grep.html>`_'s arguments.
