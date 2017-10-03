**Debugging diceroll**
=======================
**diceroll 2.3** keeps a log file of any dice rolls made during its last run. You will find ``diceroll.log`` in the ``Logs``
folder it creates if one isn't there already. In the file you will see mentions of dice being rolled. **diceroll** uses
a default logging mode of ``INFO`` which isn't that verbose. ::

   module_log.setLevel(logging.INFO)

::

   Sun, 01 Oct 2017 16:08:03 INFO diceroll - Logging started.
   Sun, 01 Oct 2017 16:08:03 INFO diceroll - roll() v2.3 started, and running...
   Sun, 01 Oct 2017 16:08:03 INFO diceroll - 3D4 = 3D4+0 = 10

Changing **diceroll's** logging mode to ``DEBUG`` will record debugging messages in the ``Logs\diceroll.log`` file. ::
   
   module_log.setLevel(logging.DEBUG)

::

   Sun, 01 Oct 2017 16:27:21 INFO diceroll - Logging started.
   Sun, 01 Oct 2017 16:27:21 INFO diceroll - roll() v2.3 started, and running...
   Sun, 01 Oct 2017 16:27:21 DEBUG diceroll - Asked to roll 3D4:
   Sun, 01 Oct 2017 16:27:21 DEBUG diceroll - Using three 4-sided dice...
   Sun, 01 Oct 2017 16:27:21 DEBUG diceroll - Rolled a 4
   Sun, 01 Oct 2017 16:27:21 DEBUG diceroll - Rolled a 2
   Sun, 01 Oct 2017 16:27:21 DEBUG diceroll - Rolled a 2
   Sun, 01 Oct 2017 16:27:21 INFO diceroll - 3D4 = 3D4+0 = 8
   
.. note::
   Running **diceroll** in ``DEBUG`` mode may create a log file that will be too huge to open. A program of yours
   left running for a long period of time could create millions of lines of recorded log entries. Fortunately, ``diceroll.log`` is
   reset each time your program is run. Also, any errors encountered will be recorded as ``ERROR`` in the log file, no
   matter which logging mode you've chosen to use.

If your own code has logging enabled for it, be sure to let **diceroll** know by changing ``your_code_name_here`` to
the name of the program you're calling ``roll()`` from. ::

   log = logging.getLogger('your_code_name_here.diceroll')
