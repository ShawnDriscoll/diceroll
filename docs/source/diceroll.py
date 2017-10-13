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
    print roll('2D6')

    Will roll two 6-sided dice
'''

from random import randint
import os
import logging

__version__ = '2.3'
__release__ = '2.3.2b'
__author__ = 'Shawn Driscoll <shawndriscoll@hotmail.com>\nshawndriscoll.blogspot.com'

diceroll_log = logging.getLogger('diceroll')
diceroll_log.setLevel(logging.INFO)

if not os.path.exists('Logs'):
    os.mkdir('Logs')

fh = logging.FileHandler('Logs/diceroll.log', 'w')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s - %(message)s',
                              datefmt = '%a, %d %b %Y %H:%M:%S')
fh.setFormatter(formatter)
diceroll_log.addHandler(fh)

diceroll_log.info('Logging started.')
diceroll_log.info('roll() v' + __version__ + ' started, and running...')

number_of_dice = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def _dierolls(dtype, dcount):
    '''
    Takes two integer arguments:
        dtype (the number of sides for the dice)
        dcount (the number of dice to roll)
    
    and returns an integer value.
    
    This function is for internal use and has no error-checking!    
    '''

    dtotal = 0
    if dcount == 1:
        diceroll_log.debug('Using %s %d-sided die...' % (number_of_dice[dcount], dtype))
    else:
        if dcount < 11:
            diceroll_log.debug('Using %s %d-sided dice...' % (number_of_dice[dcount], dtype))
        else:
            diceroll_log.debug('Using %d %d-sided dice...' % (dcount, dtype))
        
    for i in range(dcount):
        rolled = randint(1, dtype)
        if rolled == 8 or rolled == 18:
            diceroll_log.debug('Rolled an %s' % rolled)
        else:
            diceroll_log.debug('Rolled a %s' % rolled)
        dtotal += rolled
    return dtotal

def roll(dice):
    '''
    The dice types to roll are:
        'D2', 'D3', 'D4', 'D6', 'D8', 'D9', 'D10', 'D12', 'D20', 'D30',
        'D100', 'D66', 'DD', 'FLUX', 'GOODFLUX', 'BADFLUX', 'BOON', 'BANE'

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
    
    An invalid roll will return a 0.
    '''

    log = logging.getLogger('your_code_name_here.diceroll')

    # was information for this program asked for?
    if dice == 'info':
        ver = 'roll(), release version ' + __release__ + ' for Python 2.5.4'
        diceroll_log.info('Reporting: roll() release version: %s' % __release__)
        return __version__, ver

    # make inputted string argument upper case, and strip spaces
    dice = str(dice).upper().strip()

    log.debug(dice)
    diceroll_log.debug('Asked to roll %s:' % dice)

    # set dice modifier to zero.
    dice_mod = 0

    # check if FLUX dice are being rolled
    if dice == 'FLUX':
        flux1 = randint(1, 6)
        flux2 = randint(1, 6)
        rolled = flux1 - flux2
        diceroll_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled

    elif dice == 'GOODFLUX':
        flux1 = randint(1, 6)
        flux2 = randint(1, 6)
        if flux1 < flux2:
            rolled = flux2 - flux1
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled

    elif dice == 'BADFLUX':
        flux1 = randint(1, 6)
        flux2 = randint(1, 6)
        if flux1 > flux2:
            rolled = flux2 - flux1
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux2, flux1, rolled))
        else:
            rolled = flux1 - flux2
            diceroll_log.info('%s = %d - %d = %d' % (dice, flux1, flux2, rolled))
        return rolled

    # check if a BOON roll is being performed
    elif dice == 'BOON':
        die = [0, 0, 0]
        die[0] = randint(1, 6)
        die[1] = randint(1, 6)
        die[2] = randint(1, 6)
        diceroll_log.info('Start Boon roll: %d %d %d' % (die[0], die[1], die[2]))
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
        diceroll_log.info('Sorted Boon roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled
    
    # check if a BANE roll is being performed
    elif dice == 'BANE':
        die = [0, 0, 0]
        die[0] = randint(1, 6)
        die[1] = randint(1, 6)
        die[2] = randint(1, 6)
        diceroll_log.info('Start Bane roll: %d %d %d' % (die[0], die[1], die[2]))
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
        diceroll_log.info('Sorted Bane roll: %d %d %d = %d' % (die[0], die[1], die[2], rolled))
        return rolled

    # look for DD in the string (for destructive dice rolls)
    ichar1 = dice.find('DD')
    if ichar1 == -1:
        
        # if not, does the string indicate regular dice for use?
        ichar1 = dice.find('D')
    if ichar1 == 0:
        
        # only one die is being rolled
        num_dice = 1

    if ichar1 <> -1:
        if ichar1 <> 0:
            
            # how many dice are being rolled?
            num_dice = int(dice[0:ichar1])
            if num_dice < 1:
                log.error('Negative dice count! [ERROR]')
                diceroll_log.error('Number of dice = ' + str(num_dice) + ' [ERROR]')
    
        if num_dice >= 1:
            
            # is there a +/- dice modifier for the roll?
            ichar2 = dice.find('+')
            if ichar2 <> -1:
                dice_mod = int(dice[ichar2:len(dice)])
            else:
                ichar2 = dice.find('-')
                if ichar2 <> -1:
                    dice_mod = int(dice[ichar2:len(dice)])
    
            # what kind of dice are being rolled? D6? D66? etc.
            if ichar2 <> -1:
                dice_type = dice[ichar1: ichar2]
                dice_type = dice_type.rstrip()
            else:
                dice_type = dice[ichar1: len(dice)]
    
            if dice_type == 'D6':
                rolled = _dierolls(6, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D66' and num_dice == 1 and dice_mod == 0:
                roll_1 = randint(1, 6)
                roll_2 = randint(1, 6)
                rolled = roll_1 * 10 + roll_2
                diceroll_log.info('%s = %d%s+%d = %d and %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, rolled))
                return rolled
            elif dice_type == 'D100' and num_dice == 1:
                roll_1 = (randint(1, 10) - 1) * 10
                roll_2 = randint(1, 10)
                rolled = roll_1 + roll_2 + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d and %d + %d = %d' % (dice, num_dice, dice_type, dice_mod, roll_1, roll_2, dice_mod, rolled))
                return rolled
            elif dice_type == 'D10':
                rolled = _dierolls(10, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled                               
            elif dice_type == 'D20':
                rolled = _dierolls(20, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D30':
                rolled = _dierolls(30, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D12':
                rolled = _dierolls(12, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D8':
                rolled = _dierolls(8, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D4':
                rolled = _dierolls(4, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D9':
                rolled = _dierolls(9, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D3':
                rolled = _dierolls(3, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'D2':
                rolled = _dierolls(2, num_dice) + dice_mod
                diceroll_log.info('%s = %d%s+%d = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
            elif dice_type == 'DD':
                rolled = (_dierolls(6, num_dice) + dice_mod) * 10
                diceroll_log.info('%s = (%d%s+%d) * 10 = %d' % (dice, num_dice, dice_type, dice_mod, rolled))
                return rolled
                                                    
    log.error('Wrong dice type entered! [ERROR]')
    diceroll_log.error('!!!!!!!!!!!!!!!!!!!!! DICE ERROR! ' + dice + ' is unknown !!!!!!!!!!!!!!!!!!!!!!!!!')
    
    print
    print "** DICE ERROR! '%s' is unknown **" % dice
    print
    print "Valid dice rolls are:"
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
