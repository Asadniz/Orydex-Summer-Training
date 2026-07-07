"""
Automated checks for Problem 2 — p2_collection_operations.py

Spec (from task1/README.md and the function docstrings):
- list_operations: copy, add "cardiac", remove "asthma", return sorted.
- set_operations: return common, all-unique, and primary-only conditions.
"""

from p2_collection_operations import (
    follow_up_conditions,
    list_operations,
    primary_conditions,
    sample_conditions,
    set_operations,
)


def test_list_operations_result():
    # ["diabetes", "asthma", "hypertension"] -> add "cardiac", remove "asthma"
    # -> sorted -> ["cardiac", "diabetes", "hypertension"]
    assert list_operations(sample_conditions) == ["cardiac", "diabetes", "hypertension"]


def test_list_operations_does_not_mutate_input():
    before = list(sample_conditions)
    list_operations(sample_conditions)
    assert sample_conditions == before, "work on a copy; do not modify the input list"


def test_set_operations_common():
    result = set_operations(primary_conditions, follow_up_conditions)
    assert result["common"] == {"diabetes", "asthma"}


def test_set_operations_all_unique():
    result = set_operations(primary_conditions, follow_up_conditions)
    assert result["all_unique"] == {"diabetes", "asthma", "hypertension", "cardiac"}


def test_set_operations_only_primary():
    result = set_operations(primary_conditions, follow_up_conditions)
    assert result["only_primary"] == {"hypertension"}
