**What's New**
==============

.. versionadded:: 2.3

BOON and BANE rolls have been added.

.. versionadded:: 2.2

One exception to the "integer" rule for ``roll()`` is when using ``roll('info')``, which will return two strings:

>>> version, release = roll('info')
>>> print version
2.2
>>> print release
roll(), release version 2.2.1 (Beta) for Python 2.5.4