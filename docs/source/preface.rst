**Preface**
===========

Back during the release of **diceroll 2.2**, I wanted to learn something new in regards to Python. Even though I use 2.5.4,
there is still a lot about it that I have never delved into. Sphinx was something I had not really paid any mind to
in the past. It was yet another one of those *need to know only* things about Python. Some things I'd get around to
learning only when I had to, but only if it was part of something else that I had taken an interest in doing.

So somewhere in my discovering of PyMongo, I had been pointed to Sphinx and Jinja. They were both something about document
generation. And since I had just learned about Pandas and CSV, I was in a data retrieval mood still.

In a nutshell,
Sphinx is an EXE (generated during its install from an egg of .py files, which is still magic to me, and which took a
great deal of time for me tracking down all the proper versions of requirements for it to even compile/run
in Python 2.5.4) that generates documents. Nothing too fancy. Just simple documents that could be read easily/quickly
through any device using any viewer. And when I learned that Sphinx could read Python modules and produce documents
from their ``.__doc__`` strings, I knew I just had to spend a couple days learning how all that stuff happens. 

So basically, my Python dice rolling module has its own operations manual now. And some rabbit holes are
worth their going into.
