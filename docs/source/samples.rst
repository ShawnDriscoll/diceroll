**Using roll() in Your Own Code**
=================================

.. highlight:: python
   :linenothreshold: 5

For Simple Die Rolls
--------------------

Sample Outputting of Die Rolls: ::

    # import the roll() module
    from diceroll import roll

    # enter the roll type to be made
    number_of_dice = str(raw_input('Number of dice to roll? '))
    dice_type = raw_input('Dice type? ')
    dice_roll_modifier = str(raw_input('DM? '))

    # make sure that there is a plus or minus sign in the DM string
    if dice_roll_modifier[0] <> '-' and dice_roll_modifier[0] <> '+':
        dice_roll_modifier = '+' + dice_roll_modifier

    # concatenate the values for the dice string
    dice = number_of_dice + dice_type + dice_roll_modifier

    print
    print 'Rolling', dice

    # do 20 rolls
    for i in range(20):
        print 'You rolled a %d' % roll(dice)

For Probabilites
----------------

Sample Task Resolution: ::
    
    # import the roll() module
    from diceroll import roll

    # Enter your character's chances to succeed at a task
    skilled = raw_input('Is your character trained for the task ([y]/n)? ')
    if skilled == 'n':
        die_mod = -3
    else:
        die_mod = int(raw_input("Enter your character's skill level (0 to 4)? "))
    difficulty = int(raw_input('Enter the difficulty of the task\n(Impossible: -6 to Easy: +6)? '))

    # The player must roll an 8 or higher for their character to succeed
    dice_roll = roll('2D6') + die_mod + difficulty
    print
    print 'You rolled:', dice_roll
    if dice_roll >= 8:
        print 'Your character succeeds with the task.'
        if dice_roll - 8 >= 6:
            print 'Your character saved everyone.'
    else:
        print 'Your character fails at the task.'
        if dice_roll - 8 < -3:
            print 'Your character becomes injured.'
        if dice_roll - 8 < -6:
            print 'Your character died from injuries!'

Encountering Errors
-------------------
Entering an invalid string for ``roll()`` will return an error message, as well as a value of 0 from the function: ::

   print roll('3d')

.. error::

   ** DICE ERROR! '3D' is unknown **
   
   | 0
