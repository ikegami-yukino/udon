udon
===========
.. image:: https://badge.fury.io/py/udon.png
    :target: http://badge.fury.io/py/udon
.. image:: https://travis-ci.org/ikegami-yukino/udon.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/udon

Udon is a text normalizer for lengthened English expression having repeating letters.

(e.g., Udon converts "cooooooooooooooollllllllllllll" to "cool")

This module is based on the following paper:

Samuel Brody and Nicholas Diakopoulos.
Cooooooooooooooollllllllllllll!!!!!!!!!!!!!! using word lengthening to detect sentiment in microblogs.
In EMNLP2011, pp. 562-570, 2011.

http://aclweb.org/anthology//D/D11/D11-1052.pdf


Installation
============

::

 $ pip install udon


Usage
=====

Import udon
--------------------------------------------

::

 >>> import udon


Normalize sentence
--------------------------------------------

::

 >>> udon.normalize_sentence('you are coooolll!!!')
 you are cool!


- normalize_sentence(str)


Normalize sentence
--------------------------------------------

::

 >>> udon.normalize_word('okayyyyy')
 okay


- normalize_word(str)


Shorten repeated substring until threshould without dictionary
-------------------------------------------------------------------

::

 >>> udon.cut_repeat('mamisaaaaaan', 1)
 mamisan
 >>> udon.cut_repeat('okayyyyy', 2)
 okayy


- cut_repeat(str, threshould)

  * Note that this method don't use a lengthened expression normalize table (e.g., cooll -> cool).
    If you want to normalize such expression, use `normalize_word()` or `normalize_sentence()` method.

  
TODO
======================
* Support Japanese lengthened expressions

Contributions are welcome!


License
=========

- This module is licensed under MIT License.

