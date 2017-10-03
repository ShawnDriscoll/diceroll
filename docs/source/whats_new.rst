**What's New?**
===============

New in version 2.3
------------------

BOON and BANE rolls have been added. Both rolls use three 6-sided dice. A BOON roll keeps the two
highest dice, while a BANE roll keeps the two lowest dice.

New in version 2.2
------------------

One exception to the "integer" rule for ``roll()`` is when using ``roll('info')``, which will return two strings:

>>> version, release = roll('info')
>>> print version
2.2
>>> print release
roll(), release version 2.2.1 (Beta) for Python 2.5.4