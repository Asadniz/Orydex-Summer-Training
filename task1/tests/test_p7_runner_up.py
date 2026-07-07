"""
Automated checks for Problem 7 — p7_runner_up.py

HackerRank "Find the Runner-Up Score!": return the second highest distinct
value in the list of scores.
"""

from p7_runner_up import find_runner_up, sample_scores


def test_sample():
    assert find_runner_up(sample_scores) == 5


def test_consecutive_values():
    assert find_runner_up([1, 2, 3, 4, 5]) == 4


def test_ignores_duplicates_of_the_max():
    assert find_runner_up([5, 5, 4]) == 4


def test_all_negative():
    assert find_runner_up([-1, -2, -3]) == -2


def test_many_duplicates():
    assert find_runner_up([10, 10, 9, 9, 8]) == 9


def test_unsorted_input():
    assert find_runner_up([6, 2, 6, 5, 3]) == 5
