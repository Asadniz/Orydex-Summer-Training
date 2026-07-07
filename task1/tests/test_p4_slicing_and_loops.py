"""
Automated checks for Problem 4 — p4_slicing_and_loops.py

The README fixes the intent (slicing, enumerate, zip, comprehensions) but
not the exact return shapes, so loop_examples is a smoke check while the
slicing/comprehension results are validated by membership where the values
are unambiguous from the module data.
"""

from p4_slicing_and_loops import (
    comprehension_examples,
    loop_examples,
    patient_ids,
    patient_names,
    slicing_examples,
)


def _flatten(value):
    """Collect all leaf items from a value that may be a tuple/list of lists."""
    items = []
    if isinstance(value, (list, tuple)):
        for element in value:
            if isinstance(element, (list, tuple)):
                items.extend(element)
            else:
                items.append(element)
    return items


def test_loop_examples_runs_without_error():
    loop_examples()


def test_slicing_examples_contains_expected_values():
    result = slicing_examples()
    assert result is not None, "slicing_examples should return its results"
    items = _flatten(result)
    # first three, last three, and reversed should all be drawn from patient_ids
    assert patient_ids[:3] == [101, 102, 103]
    assert 101 in items and 103 in items
    assert 105 in items and 107 in items


def test_comprehension_examples_even_ids_and_upper_names():
    result = comprehension_examples()
    assert result is not None, "comprehension_examples should return its results"
    items = _flatten(result)
    expected_even = [pid for pid in patient_ids if pid % 2 == 0]  # [102, 104, 106]
    expected_upper = [name.upper() for name in patient_names]
    for value in expected_even:
        assert value in items
    assert any(name in items for name in expected_upper)
