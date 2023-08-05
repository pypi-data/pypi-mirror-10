.. :changelog:

History
#######

0.0.3 (2015-05-10)
------------------

* FIX: setup.py correctly sets packages now. Updated makefile.

* Setting empty ``__slots__`` on ``namedtuple_with_defaults``. This fixes
  ``__dict__`` and reduces memory usage.

0.0.2 (2015-04-30)
------------------

* Simpler ``NagiosLogger`` interface. (backwards incompatible)

* Feature: ``Testcase.assertSoftCalledWith`` method for mock partial call
  assertions.

* FIX: ``NagiosLogger`` was not restoring stdout.

* FIX: ``NagiosLogger`` choked when output contained empty lines.

* Feature: ``namedtuple_with_defaults`` uses a ``lambda`` instead of a
  classmethod for mutable defaults. (backwards incompatible)

0.0.1 (2015-03-29)
------------------

* Packaging
* Namedtuple with defaults
* Mock namedtuple
* NagiosLogger
* Custom TestCase
* capture_stdout
* Colors for the terminal
