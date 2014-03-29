# -*- coding: utf-8 -*-
from nose.tools import assert_equal
import udon


def test_cut_repeat():
    assert_equal(udon.cut_repeat('udoooon', 1), 'udon')
    assert_equal(udon.cut_repeat('beeeeer', 2), 'beer')


def test_normalize_word():
    assert_equal(udon.normalize_word('thanxxxx'), 'thanx')
    assert_equal(udon.normalize_word('coooooooolllll!!!!'), 'cool!')


def test_normalize_sentence():
    normalized = udon.normalize_sentence('you are coooolll!!!')
    assert_equal(normalized, 'you are cool!')
