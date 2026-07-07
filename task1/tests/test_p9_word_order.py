"""
Automated checks for Problem 9 — p9_word_order.py

HackerRank "Word Order": return the number of distinct words and their
occurrence counts, ordered by first appearance.
"""

from p9_word_order import sample_words, word_order


def test_sample():
    assert word_order(sample_words) == (3, [2, 1, 1])


def test_all_same_word():
    assert word_order(["a", "a", "a"]) == (1, [3])


def test_all_distinct():
    assert word_order(["x", "y", "z"]) == (3, [1, 1, 1])


def test_preserves_first_appearance_order():
    assert word_order(["b", "a", "b", "a", "c"]) == (3, [2, 2, 1])


def test_single_word():
    assert word_order(["hello"]) == (1, [1])
