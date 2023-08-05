.. |travis-ci| image:: https://secure.travis-ci.org/alisaifee/limits.png?branch=master
    :target: https://travis-ci.org/#!/alisaifee/limits?branch=master

|travis-ci|

********
pycrm114
********

Python bindings for libcrm114

Minimal quickstart
==================

No persistence
--------------
.. code-block:: python

    import pycrm114

    crm = pycrm114.CRM114(classes=["spam", "ham"])
    crm.learn("spam", "foo bar")
    crm.learn("ham", "bar is good")
    assert crm.classify("is bar good")["class"] == "ham"
    assert crm.classify("foo bar good")["class"] == "spam"


File System Persistence
-----------------------

.. code-block:: python

    import pycrm114

    crm = pycrm114.CRM114(classes=["spam", "ham"], storage=pycrm.storage.FileSystemStorage("/var/tmp/crm-test"))
    crm.learn("spam", "foo bar")
    crm.learn("ham", "bar is good")
    crm.save()
    new_crm = pycrm114.CRM114(classes=["spam", "ham"], storage=pycrm.storage.FileSystemStorage("/var/tmp/crm-test"))
    assert new_crm.classify("is bar good")["class"] == "ham"
    assert new_crm.classify("foo bar good")["class"] == "spam"

Dependencies
============

Debian/Ubuntu: ``sudo apt-get install libtre5 libtre-dev``

OS X: ``brew install tre``

Tests
=====

Dependencies
------------

.. code-block:: bash 

  pip install -r requirements/test.txt

To test against different python versions use tox::
  
  tox 

To run the tests with the active python::

  python setup.py build && nosetests tests 


Building
========

.. code-block:: bash

  python setup.py build

References
==========

* `crm114 <http://crm114.sourceforge.net/wiki/doku.php>`_

