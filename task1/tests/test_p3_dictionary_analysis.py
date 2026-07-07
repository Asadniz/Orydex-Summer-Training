"""
Automated checks for Problem 3 — p3_dictionary_analysis.py

Spec (from task1/README.md): access nested values, update values, read
missing keys safely with .get(), and build a summary dictionary.
"""

import copy

import p3_dictionary_analysis as p3
from p3_dictionary_analysis import (
    build_patient_summary,
    get_patient_city,
    update_patient_condition,
)


def test_get_patient_city_known():
    assert get_patient_city(1) == "Karachi"
    assert get_patient_city(2) == "Lahore"


def test_get_patient_city_missing_is_safe():
    # "Safely return the city" -> a missing patient must not raise.
    get_patient_city(999)


def test_update_patient_condition():
    original = copy.deepcopy(p3.patients)
    try:
        update_patient_condition(1, "asthma")
        assert p3.patients[1]["condition"] == "asthma"
    finally:
        # Restore module state so test order does not matter.
        p3.patients.clear()
        p3.patients.update(original)


def test_build_patient_summary_returns_dict():
    summary = build_patient_summary()
    assert isinstance(summary, dict)
    assert summary, "summary should not be empty"
