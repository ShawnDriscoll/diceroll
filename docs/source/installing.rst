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

Say you have a folder called ``library``, and assuming you have an ``__init__.py`` inside it, just copy ``diceroll.py``
into your ``library`` folder and add this line near the top of your code: ::

   from library.diceroll import roll
