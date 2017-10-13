**diceroll Tutorial**
=====================

Rolling the Dice
----------------
Once ``diceroll.py`` is installed and your code is able to import the module, its ``roll()`` function can be
used right away. This function returns an integer, by the way. So it can be used as any other integer would
be used. But first, we must give this function a value to work from.

Those of you that have used dice rolling programs before will notice that something is different. And that is,
``roll()`` uses a string for its input:

>>> die1 = roll('1D6')
>>> die2 = roll('1d6')
>>> dice = '3D4+1'
>>> print die1, die2, roll(dice)
3, 2, 9

.. versionadded:: 2.2

Notice that the inputted string values can be upper or lower case. And note that the return values are integer.

The dice types to roll are:

   D3, D4, D6, D8, D9, D10, D12, D20, D30, D100, D66, DD, FLUX, GOODFLUX, and BADFLUX

.. versionadded:: 2.3

Three additional dice types are now available:

   BOON, BANE, and D2
   
.. note::

   You may recognize some of these dice types from various tabletop role-playing games. Not all dice types are
   covered by **diceroll**. But more are plannned for in future releases of this module.

**diceroll** uses a simple standard when it comes to rolling various dice types.

Some examples are:

.. literalinclude:: databox1.dat

Encountering Errors
-------------------
Entering an invalid string for ``roll()`` will return an error message, as well as a value of 0 from the function: ::

   print roll('3d')

.. error::

   ** DICE ERROR! '3D' is unknown **
   
   | 0
