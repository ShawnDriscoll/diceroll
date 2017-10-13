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
    

.. command-output:: diceroll.roll('info')

.. literalinclude:: figure1.dat
