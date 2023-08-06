digs: easy text crawling.
====
"For those who need to extract text to some depth over a website. "

|PyPI Package latest release| |Code Quality Status|

Usage
-----
You want to extract all text data from a url website to your current directory:

::

    digs http://thewebsite.com

You can add the option `--depth=LEVEL` to perform over the root domain (website) a search to get all the text data:

::

    digs http://thewebsite.com --depth=3

Be careful, with a high level, the tree search grows exponentially. 

Also, you can use the graphical interface (if you have installed PySide):

::

    digs -i

You should something like this:

|GUI|


Installation
------------

::

    pip install digs


Requirements
^^^^^^^^^^^^
::

    requirements.txt


`digs` was written by `Jonathan S. Prieto C. <prieto.jona@gmail.com>`_.


.. |PyPI Package latest release| image:: http://img.shields.io/pypi/v/digs.png?style=flat
   :target: https://pypi.python.org/pypi/digs
.. |Code Quality Status| image:: https://landscape.io/github/d555/digs/master/landscape.svg?style=flat
   :target: https://landscape.io/github/d555/digs/master
.. |GUI| image:: https://raw.githubusercontent.com/d555/digs/master/gui.png
   :target: https://pypi.python.org/pypi/digs
