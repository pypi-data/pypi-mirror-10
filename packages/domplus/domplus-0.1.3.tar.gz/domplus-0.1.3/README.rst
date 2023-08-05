=======
domplus
=======

.. image:: https://travis-ci.org/eabps/domplus.png?branch=master
		:target: https://travis-ci.org/eabps/domplus
		:alt: Test Status

.. image:: https://landscape.io/github/eabps/domplus/master/landscape.png
		:target: https://landscape.io/github/eabps/domplus/master
		:alt: Code Helth

.. image:: https://pypip.in/v/domplus/badge.svg
		:target: https://pypi.python.org/pypi//domplus/
		:alt: Latest PyPI version

.. image:: https://pypip.in/d/domplus/badge.svg
		:target: https://pypi.python.org/pypi//domplus/
		:alt: Downloads

.. image:: https://badges.gitter.im/Join%20Chat.svg
		:target: https://gitter.im/eabps/domplus?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
		:alt: Chat

domplus is a python package with common functions for commercial applications.

Features
--------

* Check if string is brazilian CPF valid
* Check if string is brazilian CNPJ valid
* Check if string is brazilian CPF valid or brazilian CNPJ valid
* Check if credit card number is valid

Installation
------------

.. code-block:: console

    pip install domplus

Usage govplus
-------------

.. code-block:: python

 from domplus import govplus

 # Check if string is brazilian CPF valid. Return True or False
 govplus.is_valid_br_cpf("03167158590")

 # OR
 govplus.is_valid_br_cpf("031.671.585-90")

 # Check if string is brazilian CNPJ valid. Return True or False
 govplus.is_valid_br_cnpj("75317134000130")

 # OR
 govplus.is_valid_br_cnpj("75.317.134/0001-30")

 # Check if string is brazilian CPF valid or brazilian CNPJ valid.
 # Return "cpf", "cnpj" or False
 govplus.is_br_cpf_or_cnpj("03167158590")

 # OR
 govplus.is_br_cpf_or_cnpj("031.671.585-90")

 # OR
 govplus.is_br_cpf_or_cnpj("75317134000130")

 # OR
 govplus.is_br_cpf_or_cnpj("75.317.134/0001-30")


Usage financeplus
-----------------

.. code-block:: python
 
 from domplus import financeplus

 # Check if string is a Credcard Number valid.
 # Return True or False
 financeplus.is_valid_creditcard("374356783424314")