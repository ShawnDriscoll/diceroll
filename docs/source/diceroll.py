#
#   Written for Python 2.5.4
#
#   To use this module: from diceroll import roll
#
#   Make a dice roll
#
##########################################################

'''
Usage:
    from diceroll import roll
    
    print roll('2D6') - roll two 6-sided dice
'''

from random import randint
import os
import logging

__version__ = '2.3'
__release__ = '2.3.0 (Beta)'
__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'

module_log = logging.getLogger('diceroll')
module_log.setLevel(logging.INFO)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

fh = logging.FileHandler('Logs/diceroll.log', 'w')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                              datefmt = '%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
module_log.addHandler(fh)

module_log.info('Logging started.')
module_log.info('roll() v' + __version__ + ' started, and running...')

number_of_dice = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def die_rolls(dtype, dcount):
    '''
    Two arguments:
    
      dtype: the number of sides for the dice (int)
      dcount: the number of dice to roll (int)
    
    Value returned:
    
      dtotal: the value returned from die_rolls (int)
    '''

    dtotal = 0
    if dcount == 1:
        module_log.debug('Using %s %d-sided die...' % (number_of_dice[dcount], dtype))
    else:
        if dcount < 11:
            module_log.debug('Using %s %d-sided dice...' % (number_of_dice[dcount], dtype))
        else:
            module_log.debug('Using %d %d-sided dice...' % (dcount, dtype))
        
    for i in range(dcount):
        rolled = randint(1, dtype)
        if rolled == 8 or rolled == 18:
            module_log.debug('Rolled an %s' % rolled)
        else:
            module_log.debug('Rolled a %s' % rolled)
        dtotal += rolled
    return dtotal

def roll(dice):
    '''
    The dice types to roll are: D3, D4, D6, D8, D9, D10, D12, D20, D30, D100, D66, DD, FLUX, GOODFLUX, BADFLUX

    Some examples are:
    
    roll('D6') or roll('1D6') -- roll one 6-sided die
    
    roll('2D6') -- roll two 6-sided dice
    
    roll('D10') -- roll a 10-sided die (1 - 10)
    
    roll('D100') -- roll a 100-sided die (1 - 100)
    
    roll('D66') -- roll for a D66 chart
    
    roll('FLUX') -- a FLUX roll (-5 to 5)

    roll('3D6+6') -- add +6 DM to roll
    
    roll('4D4-4') -- add -4 DM to roll
    
    roll('2DD+3') -- roll (2D6+3) x 10
    
    roll('BOON') -- roll 3D6 and keep the higher two dice
    
    roll('info') -- release version of program
    
    An invalid roll will return a 0 (int).
    '''

    log = logging.getLogger('your_code_name_here.diceroll')

    if dice == 'info':
        ver = 'roll(), release version ' + __release__ + ' for Python 2.5.4'
        module_log.info('Reporting: roll() release version: %s' % __release__)
        return __version__, ver

    dice = str(dice).upper().strip()

    log.debug(dice)
    module_log.debug('Asked to roll %s:' % dice)

    dice_mod = 0

    if dice == 'FLUX':
        flux1 = randint(1, 6)
        flux2 = randint(1, 6)
        rolled = flux1 - flux2
        module_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled
    elif dice == 'GOODFLUX':
        flux1 = randint(1, 6)
        flux2 = randint(1, 6)
        if flux1 < flux2:
            rolled = flux2 - flux1
            module_log.info('%s = %d - %d = %d' % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            module_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled
    elif dice == 'BADFLUX':
        flux1 = randint(1, 6)
        flux2 = randint(1, 6)
        if flux1 > flux2:
            rolled = flux2 - flux1
            module_log.info('%s = %d - %d = %d' % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            module_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled
    elif dice == 'BOON':
        die = [0, 0, 0]
        die[0] = randint(1, 6)
        die[1] = randint(1, 6)
        die[2] = randint(1, 6)
        module_log.info('Start Boon roll: %d %d %d' % (die[0], die[1], die[2]))
        die_swap = True
        while die_swap == True:
            die_swap = False
            for j in range(2):
                if die[j] < die[j+1]:
                    temp_die = die[j]
                    die[j] = die[j+1]
                    die[j+1] = temp_die
                    die_swap = True
        rolled = die[0] + die[1]
        module_log.info('Sorted Boon roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled
    elif dice == 'BANE':
        die = [0, 0, 0]
        die[0] = randint(1, 6)
        die[1] = randint(1, 6)
        die[2] = randint(1, 6)
        module_log.info('Start Bane roll: %d %d %d' % (die[0], die[1], die[2]))
        die_swap = True
        while die_swap == True:
            die_swap = False
            for j in range(2):
                if die[j] > die[j+1]:
                    temp_die = die[j]
                    die[j] = die[j+1]
                    die[j+1] = temp_die
                    die_swap = True
        rolled = die[0] + die[1]
        module_log.info('Sorted Bane roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled

    ichar1 = dice.find('DD')
    if ichar1 == -1:
        ichar1 = dice.find('D')
    if ichar1 == 0:
        num_dice = 1

    if ichar1 <> -1:
        if ichar1 <> 0:
            num_dice = int(dice[0:ichar1])
    #        print 'Number of dice =', num_dice
            if num_dice < 1:
                log.error('Negative dice count! [ERROR]')
                module_log.error('Number of dice = ' + str(num_dice) + ' [ERROR]')
    
        if num_dice >= 1:
            ichar2 = dice.find('+')
            if ichar2 <> -1:
                dice_mod = int(dice[ichar2:len(dice)])
    #            print 'dice mod =', dice_mod
            else:
                ichar2 = dice.find('-')
                if ichar2 <> -1:
                    dice_mod = int(dice[ichar2:len(dice)])
    #                print 'dice mod =', dice_mod
    
            if ichar2 <> -1:
                dice_type = dice[ichar1: ichar2]
                dice_type = dice_type.rstrip()
            else:
                dice_type = dice[ichar1: len(dice)]
    #            print 'dice type =', dice_type, 'Len = ', len(dice_type)
    
            if dice_type == 'D6':
                rolled = die_rolls(6, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D66' and num_dice == 1 and dice_mod == 0:
                roll_1 = randint(1, 6)
                roll_2 = randint(1, 6)
                rolled = roll_1 * 10 + roll_2
                module_log.info('%s = %d%s+%d = %d and %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, rolled))
                return rolled
            elif dice_type == 'D100' and num_dice == 1:
                roll_1 = (randint(1, 10) - 1) * 10
                roll_2 = randint(1, 10)
                rolled = roll_1 + roll_2 + dice_mod
                module_log.info('%s = %d%s+%d = %d and %d + %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
            elif dice_type == 'D10':
                rolled = die_rolls(10, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled                               
            elif dice_type == 'D20':
                rolled = die_rolls(20, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D30':
                rolled = die_rolls(30, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D12':
                rolled = die_rolls(12, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D8':
                rolled = die_rolls(8, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D4':
                rolled = die_rolls(4, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D9':
                rolled = die_rolls(9, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D3':
                rolled = die_rolls(3, num_dice) + dice_mod
                module_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'DD':
                rolled = (die_rolls(6, num_dice) + dice_mod) * 10
                module_log.info('%s = (%d%s+%d) * 10 = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
                                                    
    log.error('Wrong dice type entered! [ERROR]')
    module_log.error('!!!!!!!!!!!!!!!!!!!!! DICE ERROR! ' + dice + ' is unknown !!!!!!!!!!!!!!!!!!!!!!!!!')
    
    print
    print "** DICE ERROR! '%s' is unknown **" % dice
    print
    print "The types of dice to roll are (in string values):"
    print "roll('D6') or roll('1D6') -- roll one 6-sided die"
    print "roll('2D6') -- roll two 6-sided dice"
    print "roll('D10') -- roll a 10-sided die (1 - 10)"
    print "roll('D100') -- roll a 100-sided die (1 - 100)"
    print "roll('D66') -- roll for a D66 chart"
    print "roll('FLUX') -- a FLUX roll (-5 to 5)"
    print "roll('2DD+3') -- roll (2D6+3) x 10"
    print "roll('BOON') -- roll 3D6 and keep the higher two dice"
    print
    print "-/+ DMs can be added to rolls:"
    print "roll('3D6+6') -- add +6 DM to roll"
    print "roll('4D4-4') -- add -4 DM to roll"
    print
    print "roll('info') -- release version of program"
    print
    return 0
