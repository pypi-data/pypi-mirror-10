Digs
====

Just making easy the text crawling task over websites.

|PyPI Package latest release| |Code Quality Status| |PyPI Package
monthly downloads| |GitHub issues for digs|

Usage
=====

You want to extract all text data from a url website to your current
directory:

::

    digs http://thewebsite.com

You can add the option --depth=LEVEL to perform over the root domain
(website) a search to get all the text data:

::

    digs http://thewebsite.com --depth=3

Be careful, with a high level, the tree search grows exponentially.

Also, you can use the graphical interface (if you have installed
PySide):

::

    digs -i

You should something like this:

|GUI|

Installation
============

::

    pip install digs

Requirements
------------

::

    requirements.txt

digs was written by `Jonathan S. Prieto C. <prieto.jona@gmail.com>`__.

.. |PyPI Package latest release| image:: http://img.shields.io/pypi/v/digs.png?style=flat
   :target: https://pypi.python.org/pypi/digs
.. |Code Quality Status| image:: https://landscape.io/github/d555/digs/master/landscape.svg?style=flat
   :target: https://landscape.io/github/d555/digs/master
.. |PyPI Package monthly downloads| image:: http://img.shields.io/pypi/dm/digs.png?style=flat
   :target: https://pypi.python.org/pypi/digs
.. |GitHub issues for digs| image:: https://img.shields.io/github/issues/d555/digs.svg?style=flat-square
   :target: https://github.com/d555/digs/issues
.. |GUI| image:: https://raw.githubusercontent.com/d555/digs/master/gui.png
   :target: https://pypi.python.org/pypi/digs
