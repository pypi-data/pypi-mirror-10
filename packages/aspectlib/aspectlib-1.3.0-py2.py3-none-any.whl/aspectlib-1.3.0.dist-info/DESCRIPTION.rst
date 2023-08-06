================
python-aspectlib
================

| |docs| |travis| |appveyor| |coveralls| |landscape| |scrutinizer|
| |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-aspectlib/badge/?style=flat
    :target: https://readthedocs.org/projects/python-aspectlib
    :alt: Documentation Status

.. |travis| image:: http://img.shields.io/travis/ionelmc/python-aspectlib/master.png?style=flat
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-aspectlib

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-aspectlib?branch=master
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-aspectlib

.. |coveralls| image:: http://img.shields.io/coveralls/ionelmc/python-aspectlib/master.png?style=flat
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-aspectlib

.. |landscape| image:: https://landscape.io/github/ionelmc/python-aspectlib/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/python-aspectlib/master
    :alt: Code Quality Status

.. |version| image:: http://img.shields.io/pypi/v/aspectlib.png?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/aspectlib

.. |downloads| image:: http://img.shields.io/pypi/dm/aspectlib.png?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/aspectlib

.. |wheel| image:: https://pypip.in/wheel/aspectlib/badge.png?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/aspectlib

.. |supported-versions| image:: https://pypip.in/py_versions/aspectlib/badge.png?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/aspectlib

.. |supported-implementations| image:: https://pypip.in/implementation/aspectlib/badge.png?style=flat
    :alt: Supported imlementations
    :target: https://pypi.python.org/pypi/aspectlib

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/python-aspectlib/master.png?style=flat
    :alt: Scrtinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-aspectlib/

``aspectlib`` is an aspect-oriented programming, monkey-patch and decorators library. It is useful when changing
behavior in existing code is desired. It includes tools for debugging and testing: simple mock/record and a complete
capture/replay framework.


Documentation
=============

Docs are hosted at readthedocs.org: `python-aspectlib docs <http://python-aspectlib.readthedocs.org/en/latest/>`_.

Implementation status
=====================

Weaving functions, methods, instances and classes is completed.

Pending:

* *"Concerns"* (see `docs/todo.rst`)

If ``aspectlib.weave`` doesn't work for your scenario please report a bug !

Requirements
============

:OS: Any
:Runtime: Python 2.6, 2.7, 3.3, 3.4 or PyPy

Python 3.2, 3.1 and 3.0 are *NOT* supported (some objects are too crippled).

Similar projects
================

* `function_trace <https://github.com/RedHatQE/function_trace>`_ - extremely simple

Changelog
=========

1.3.0 (2015-06-06)
------------------

* Added ``messages`` property to ``obj``. Change ``call`` to have level name instead of number.
* Fixed a bogus warning from ``func``` when patching methods on old style classes.

1.2.2 (2014-11-25)
------------------

* Added support for weakrefs in the ``__logged__`` wrapper from ``obj`` decorator.

1.2.1 (2014-10-15)
------------------

* Don't raise exceptions from ``Replay.__exit__`` if there would be an error (makes original cause hard to debug).

1.2.0 (2014-06-24)
------------------

* Fixed weaving methods that were defined in some baseclass (and not on the target class).
* Fixed wrong qualname beeing used in the Story/Replay recording. Now used the alias given to the weaver instead of
  whatever is the realname on the current platform.

1.1.1 (2014-06-14)
------------------

* Use ``ASPECTLIB_DEBUG`` for every logger in ``aspectlib``.

1.1.0 (2014-06-13)
------------------

* Added a `bind` option to ``obj`` so you can access the cutpoint from the advisor.
* Replaced automatic importing in ``obj`` with extraction of context variables (locals and globals
  from the calling ``obj``). Works better than the previous inference of module from AST of the
  result.
* All the methods on the replay are now properties: ``obj``,
  ``obj`` and ``obj``.
* Added ``obj`` and ``obj``.
* Added an ``ASPECTLIB_DEBUG`` environment variable option to switch on debug logging in ``aspectlib``'s internals.

1.0.0 (2014-05-03)
------------------

* Reworked the internals ``obj`` to keep call ordering, to allow dependencies and improved the
  serialization (used in the diffs and the missing/unexpected lists).


0.9.0 (2014-04-16)
------------------

* Changed ``obj``:

    * Renamed `history` option to `calls`.
    * Renamed `call` option to `iscalled`.
    * Added `callback` option.
    * Added `extended` option.

* Changed ``obj``:

    * Allow weaving everything in a module.
    * Allow weaving instances of new-style classes.

* Added ``obj`` class for capture-replay and stub/mock testing.

0.8.1 (2014-04-01)
------------------

* Use simpler import for the py3support.

0.8.0 (2014-03-31)
------------------

* Change ``obj`` to use ``obj`` and work as expected with coroutines or generators.
* Fixed ``obj`` to work on Python 3.4.
* Remove the undocumented ``aspectlib.Yield`` advice. It was only usable when decorating generators.

0.7.0 (2014-03-28)
------------------

* Add support for decorating generators and coroutines in ``obj``.
* Made aspectlib raise better exceptions.

0.6.1 (2014-03-22)
------------------

* Fix checks inside ``obj`` that would inadvertently call ``__bool__``/``__nonzero``.

0.6.0 (2014-03-17)
------------------

* Don't include __getattribute__ in ALL_METHODS - it's too dangerous dangerous dangerous dangerous dangerous dangerous
  ... ;)
* Do a more reliable check for old-style classes in debug.log
* When weaving a class don't weave attributes that are callable but are not actually routines (functions, methods etc)

0.5.0 (2014-03-16)
------------------

* Changed ``obj``:

    * Renamed `arguments` to `call_args`.
    * Renamed `arguments_repr` to `call_args_repr`.
    * Added `call` option.
    * Fixed issue with logging from old-style methods (object name was a generic "instance").

* Fixed issues with weaving some types of builtin methods.
* Allow to apply multiple aspects at the same time.
* Validate string targets before weaving. ``aspectlib.weave('mod.invalid name', aspect)`` now gives a clear error
  (``invalid name`` is not a valid identifier)
* Various documentation improvements and examples.

0.4.1 (2014-03-08)
------------------

* Remove junk from 0.4.0's source distribution.

0.4.0 (2014-03-08)
------------------

* Changed ``obj``:

    * Replaced `only_methods`, `skip_methods`, `skip_magicmethods` options with `methods`.
    * Renamed `on_init` option to `lazy`.
    * Added `aliases` option.
    * Replaced `skip_subclasses` option with `subclasses`.

* Fixed weaving methods from a string target.

0.3.1 (2014-03-05)
------------------

* ???

0.3.0 (2014-03-05)
------------------

* First public release.


