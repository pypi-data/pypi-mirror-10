.. |travis-ci| image:: https://secure.travis-ci.org/alisaifee/pycrm114.png?branch=master
    :target: https://travis-ci.org/#!/alisaifee/pycrm114?branch=master
.. |coveralls| image:: https://coveralls.io/repos/alisaifee/pycrm114/badge.png?branch=master
    :target: https://coveralls.io/r/alisaifee/pycrm114?branch=master
.. |pypi| image:: https://pypip.in/v/pycrm114/badge.png
    :target: https://crate.io/packages/pycrm114/
.. |license| image:: https://pypip.in/license/pycrm114/badge.png
    :target: https://pypi.python.org/pypi/pycrm114/
.. _crm114: http://crm114.sourceforge.net/wiki/doku.php

|travis-ci| |coveralls| |pypi| |license|

********
pycrm114
********

Pythonic bindings for `crm114`_

CRM114 - the Controllable Regex Mutilator
=========================================

    CRM114 is a system to examine incoming e-mail, system log streams, data files or other
    data streams, and to sort, filter, or alter the incoming files or data streams according
    to the user's wildest desires.

    -- crm114.sourceforge.net


Quickstart
==========

No persistence
--------------
.. code-block:: python

    import pycrm114

    crm = pycrm114.CRM114(classes=["spam", "ham"])
    crm.learn("spam", "foo bar")
    crm.learn("ham", "bar is good")
    assert crm.classify("is bar good")["class"] == "ham"
    assert crm.classify("foo bar good")["class"] == "spam"
    crm.forget("spam", "foo bar")
    assert crm.classify("foo bar good")["class"] == "ham"


File System Persistence
-----------------------

.. code-block:: python

    import pycrm114

    crm = pycrm114.CRM114(
        classes=["spam", "ham"],
        storage=pycrm.storage.FileSystemStorage("/var/tmp/crm-test")
    )
    crm.learn("spam", "foo bar")
    crm.learn("ham", "bar is good")
    crm.save()
    new_crm = pycrm114.CRM114(
        classes=["spam", "ham"],
        storage=pycrm.storage.FileSystemStorage("/var/tmp/crm-test")
    )
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

* `crm114`_ 

