===========
pyodcompare
===========

Provides a command line and a class
to generate an odt file which is a comparison between two documents.

You need a soffice / libreoffice service listening on a port (2002 by default)

	>>> from pyodcompare import DocumentCompare
	>>> compare = DocumentCompare(listener=('localhost', 2002))
	>>> compare.compare('reportV2.doc', 'reportV1.doc', 'reportdiff.odt')

This creates the file reportdiff.odt with a comparison of reportV2.doc (new )
reportV1.doc (original version)

This uses UNO bridge

Installation
------------

Works with python 2 and python 3, since python-uno is installed at system level for this 

sudo apt-get install python-uno

or 

sudo apt-get install python3-uno

It depends on your system. Then,

easy_install pyodcompare

Tests
=====

This add-on is tested using Travis CI. The current status of the add-on is :

.. image:: https://secure.travis-ci.org/tdesvenain/pyodcompare.png
    :target: http://travis-ci.org/tdesvenain/pyodcompare

Credits
=======

Thomas Desvenain thomas.desvenain@gmail.com

This product is based on the model of PyODConverter
_`https://pypi.python.org/pypi/PyODConverter`

The code has been inspired by this script :
_`http://win32com.goermezer.de/content/view/193/274/`
