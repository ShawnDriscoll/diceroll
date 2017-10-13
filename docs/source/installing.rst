**Installing diceroll**
=======================

Local Installation
------------------

Installing **diceroll 2.3** is as easy as always. Just copy ``diceroll.py`` into the same folder
your code happens to be in.

Then add this line at (or near) the top of your code: ::

   from diceroll import roll

Packaged Installation
---------------------

If your code setup is different, in that you like to keep your function modules in a folder separate
from your main code, you could copy ``diceroll.py`` into that folder.

Say you have a folder called ``game_utils``, and assuming you have an ``__init__.py`` inside it, just copy ``diceroll.py``
into your ``game_utils`` folder and add this line near the top of your code: ::

   from game_utils.diceroll import roll
   
Automated Installation
----------------------

Extract ``diceroll.zip`` and start a CMD window at the folder location of the ``setup.py`` file. At the
CMD prompt you can type: ::

    setup.py install

or: ::

    python setup.py install

depending on if your computer knows how to open .py files or not.


.. note::

    During the installation process,
    a ``Python25\Lib\site-packages\game_utils`` folder will be created. It will contain ``__init__.py`` and ``diceroll.py`` if your Python
    doesn't have ``setuptools`` installed. Otherwise, an .egg file called ``diceroll-2.3.1b-py2.5.egg`` will be
    created and copied into the ``Python25\Lib\site-packages`` folder.
    
No matter the automated installation that your Python performed, importing will be the same: ::

    from game_utils.diceroll import roll

Some ways to see if the ``diceroll`` module was installed correctly is by typing:

>>> print roll('info')
('2.3', 'roll(), release version 2.3.1b for Python 2.5.4')
>>> print roll.__doc__
    The dice types to roll are:
        'D3', 'D4', 'D6', 'D8', 'D9', 'D10', 'D12', 'D20', 'D30',
        'D100', 'D66', 'DD', 'FLUX', 'GOODFLUX', 'BADFLUX'
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