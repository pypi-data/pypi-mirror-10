#################################################
  ``tox-cmake``: Build CMake projects using Tox
#################################################


:author: Andre Caron (andre.l.caron@gmail.com)


Introduction
============

I guess this projects needs a bit of explaning :-)

I work on a product that uses Python on the back-end and C++ for the
client-side SDK.  Testing that the C++ client SDK and the Python back-end
quickly becomes painful.  Since Python has IMHO much, much better testing
tools, it's only natural to want to use them all the time.

Calling ``cmake`` directly from Tox's ``commands`` setting works, but it has a
few quirks:
* ``cmake`` has to be in ``PATH`` for thos to work, which makes requiring a
  specific CMake version kind of hard;
* there can be only one ``cmake`` in ``PATH``, which makes it impossible to
  test against multiple CMake versions with the same ``tox.ini`` configuration;
  and
* Tox warns when it invokes a command-line tool that isn't installed in the
  virtual environment (e.g. when it resorts to searching ``PATH`` to invoke a
  command).

This Python package is simply a stub for CMake that will accept a CMake version
requirement and find a compatible ``cmake`` program installed on your machine
(or fail with a clear error).

Since it uses a ``setuptools`` console entry-point, it also conveniently
silences Tox's warning about relying on ``PATH``.


Usage
=====

The process is quite simple:

#. Add ``tox-cmake`` to Tox's ``deps`` setting.
#. Use Tox's ``changedir`` setting (for out-of-source CMake builds).
#. Invoke ``tox-cmake`` in Tox's ``commands`` setting.

Here's a full example::

   [testenv]
   deps =
     tox-cmake
   changedir = {toxinidir}/build/{envname}
   commands =
     tox-cmake ">=2.8" ../.. -G "..."

CMake version requirements
--------------------------

The CMake version requirement string should feel familiar:

* similar to ``requirements.txt`` files, it accepts ``>=``, ``<`` and ``==``
  constraints;
* for ``>=`` and ``<`` constraints, you can specify partial version numbers
  (e.g. only major and minor);
* for ``==`` constraints, you need to have an exact match;
* a small extension allows picking a taggerd build (e.g. ``"-foo"`` will pick a
  version like ``2.8.12.2-foo``)
* commas allow to specify multiple constraints (e.g. ">=2.8,<3" will search for
  the latest CMake 2.8 on your system).


Licensing and redistribution
============================

The project is released under the MIT license.  See the ``LICENSE.txt`` file
for legal text.


Contributing
============

Pull requests are welcome!
