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

Two additional dice types are now available:

   BOON and BANE
   
.. note::

   You may recognize some of these dice types from various tabletop role-playing games. There is probably a
   standard notation for dice rolls used in games. But each game typically uses its own notation.

   | **diceroll** uses a simple standard when it comes to rolling various dice types.
   |
   | Some examples are:
   |
   | roll('D6') or roll('1D6') -- roll one 6-sided die
   | roll('2D6') -- roll two 6-sided dice
   | roll('D10') -- roll a 10-sided die (1 - 10)
   | roll('D100') -- roll a 100-sided die (1 - 100)
   | roll('D66') -- roll for a D66 chart
   | roll('FLUX') -- a FLUX roll (-5 to 5)
   | roll('3D6+6') -- add +6 DM to roll
   | roll('4D4-4') -- add -4 DM to roll
   | roll('2DD+3') -- roll (2D6+3) x 10
   | roll('BOON') -- roll 3D6 and keep the higher two dice

Encountering Errors
-------------------
Entering an invalid string for ``roll()`` will return an error message, as well as a value of 0 from the function: ::

   print roll('3d')

.. error::

   ** DICE ERROR! '3D' is unknown **
   
   | 0
