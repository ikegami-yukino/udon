# -*- coding: utf-8 -*-
"""
udon - Universal Document Normalizer

This module normalizes lengthened English expression having repeating letters.
(e.g., this module converts "cooooooooooooooollllllllllllll" to "cool")

This module is based on the following paper:
Samuel Brody and Nicholas Diakopoulos.
Cooooooooooooooollllllllllllll!!!!!!!!!!!!!! using word lengthening to detect sentiment in microblogs.
In EMNLP2011, pp. 562-570, 2011.
http://aclweb.org/anthology//D/D11/D11-1052.pdf


Author:
    Yukino Ikegami

Lisence:
    MIT License

Usage:
    import udon
    text = udon.normalize_word(text) # Normalization for a word
    text = udon.normalize_sentence(text) # Normalization for a sentence
"""
from sys import version_info
import re
from . import _conv_table

re_symbol = re.compile('[^a-zA-Z0-9]{2,256}$')

if version_info < (3, 0, 0):
    range = xrange


def cut_repeat(text, threshold):
    """Reduce repeated characters until threshold
    Param:
        <str> text
        <int> threshould
    Return:
        <str> result
    """
    text = list(text)
    result = text[0]
    count = 0
    for i in range(1, len(text)):
        if text[i - 1] == text[i]:
            count += 1
            if count < threshold:
                result += text[i]
        else:
            count = 0
            result += text[i]
    return result


def normalize_word(word):
    """Normalize repeat expression for English
    Param:
        <str> word
    Return:
        <str> normalized_word
    """
    suffix_symbol = re_symbol.findall(word)
    if suffix_symbol:
        word = word.replace(suffix_symbol[0], '')
    word = cut_repeat(word, 2)
    word = _conv_table.english.get(word, word)
    return (word + cut_repeat(suffix_symbol[0], 1)) if suffix_symbol else word


def normalize_sentence(sentence):
    """Normalize for each word
    Param:
        <str> sentence
    Return:
        <str> normalized_sentence
    """
    return ' '.join([normalize_word(word) for word in sentence.split()])
