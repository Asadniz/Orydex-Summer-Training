"""
Automated checks for Problem 8 — p8_minion_game.py

HackerRank "The Minion Game": Kevin scores vowel-started substrings, Stuart
scores consonant-started substrings; a letter at index i adds (n - i) points.
"""

from p8_minion_game import minion_game


def test_banana_stuart_wins():
    # B,N,N start consonant substrings: 6+4+2 = 12; A,A,A: 5+3+1 = 9
    assert minion_game("BANANA") == "Stuart 12"


def test_kevin_wins():
    # "AB": A (vowel) -> 2, B (consonant) -> 1
    assert minion_game("AB") == "Kevin 2"


def test_draw():
    # "BAAB": Stuart 4+1 = 5, Kevin 3+2 = 5
    assert minion_game("BAAB") == "Draw"


def test_single_vowel():
    assert minion_game("A") == "Kevin 1"


def test_single_consonant():
    assert minion_game("B") == "Stuart 1"
