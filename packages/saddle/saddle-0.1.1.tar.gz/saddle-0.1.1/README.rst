Saddle
======

Saddle is a black box testing framework built upon python's unittest that
helps you write simple, easy to read functional tests for any software.

It was initially built to test Django applications, but it can be used to
write python tests for any application at all, *written in almost any
language* (PHP, Java, etc.). It is particularly well suited to testing
software that is built upon many interacting services.

Saddle is currently EXPERIMENTAL. There will be bugs lurking and APIs may
change. However, since few people are using it I will be quick to provide
support and more open to feature requests during this period. It has been
tested on Ubuntu the most, but should work on Mac OS X and (partially) on
Windows.

There are currently modules that will run PostgreSQL, Django, Redis and a
mock SMTP server (SaddleSMTP), although writing your own module is easy.
Requests to include new modules are also welcome.


Getting Started
===============

There is currently one tutorial for Saddle:

* Getting started testing with Saddle and Django, Celery, Redis and Postgresql (INCOMPLETE)

If you want a tutorial for your stack, drop me a line.



How does it work?
=================

At the heart of Saddle is the service engine, which runs one or more services
together.

A service is something like postgresql, django, redis, celery or any
equivalent that is being tested and/or is required for your system to run.

The service engine is responsible for doing the following before the test
starts, (in parallel):

* Preparing & starting services.
* Installing fixtures (databases, settings files, etc.)
* Ascertaining service and application readiness.

During the test:

* Aggregating service logs and presenting them to the user.
* Changing the system clock time that the services see as the test requires.
* Detecting error conditions/services that stop prematurely.
* 'Snapshotting' and skipping portions of tests to get quicker feedback.
* Pausing where the user requests it and breaking into IPython shell.

After the test has finished:

* Shutting down and cleaning up after the services.


Saddle Design
=============

Saddle was built to accommodate tests that follow the following principles,
as well as to follow them itself where applicable:

* Loose coupling
* Fail fast
* DRY
* FIRST principles of good tests:
** Fast
** Isolated
** Repeatable
** Self-verifying
** Timely



Caveats and Known issues
========================

* Libfaketime, which fakes the time has the following issues:
** Does not work with node.js
** Does not work correctly with Java
** Does not work on Windows

* Saddle has not been tested on Windows, Mac OS, BSD or Linux distributions
other than Ubuntu 14.04.2 LTS (kernel version : 3.13.0-49.81). Please
report any issues you have on your specific OS.

* Saddle has been tested with Django version 1.8 but not earlier versions
and DjangoService likely does not work with them (easy enough to adapt though).

* Hitting ctrl-C before the end can sometimes leave services still alive and
screw up the terminal.

* Services that are left still alive on previous test runs are not properly
killed before starting again.

* The .saddle directory should be manually cleared each time before running
a test (if faketime is used).

* The stacktrace printed after an exception in a test (before showing ipython)
does not contain the error.

* The code is mossing a lot of docstrings.

* Errors which occur during setUp will not cause test failure immediately due
to the harness thread continuing until timeout.

* Won't run with nosetests.

* Only works on python 2.


Thanks
======

Thanks to Wolfgang Hommel for the libfaketime library, which is included
as part of saddle.

