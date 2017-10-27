**diceroll Tutorial**
=====================

.. figure:: dice_tut.png

Rolling the Dice
----------------
Once ``diceroll.py`` is installed and your code is able to import the module, its ``roll()`` function can be
used right away. This function returns an integer, by the way. So it can be used as any other integer would
be used. But first, we must give this function a value to work from.

.. function:: roll(dice)

   | *dice* = a string of three ordered concatenated values:
   |
   | *number_of_dice* + *dice_type* + *dice_roll_modifier*
   |
   | As examples:
   | *dice* = '2' + 'D10' + '-2'
   | *dice* = str(3) + 'D6' + '+2'
   | *dice* = 'FLUX'
   |
   | *dice_roll_modifier* must include a '+' or '-' with its value.
   |
   | Note that both *number_dice* and *dice_roll_modifier* are optional, and may
   | not even be used by some *dice_type* rolls.

Those of you that have used dice rolling programs before will notice that something is different. And that is,
``roll()`` uses a string for its input:

>>> die1 = roll('1D6')
>>> die2 = roll('1d6')
>>> dice = '3D4+1'
>>> print die1, die2+4, roll(dice)
3, 6, 9

The return values from ``roll()`` are always integer.

*New in version 2.2*

Notice that the inputted string values can be upper or lower case.

The dice types to roll are:

   D3, D4, D6, D8, D9, D10, D12, D20, D30, D100, D66, DD, FLUX, GOODFLUX, and BADFLUX

*New in version 2.3*

Three additional dice types are now available:

   BOON, BANE, and D2

.. note::

   You may recognize some of these dice types from various tabletop role-playing games. Not all dice types are
   covered by **diceroll**. However, more are planned for in future releases.

**diceroll** uses a simple standard when it comes to rolling various dice types.

Some examples are:

.. literalinclude:: databox1.dat

*Deprecated in version 1.9.*

D00 has been replaced with D100.

*New in version 2.4*

**diceroll** can now be used directly at a CMD prompt:

.. literalinclude:: databox2.dat