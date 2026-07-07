"""
Automated checks for Problem 1 — p1_patient_summary.py

Spec (from task1/README.md):
total patients, average age, active patient count, unique conditions,
and patient count by condition.
"""

import pytest

from p1_patient_summary import (
    average_age,
    count_active_patients,
    count_by_condition,
    patients,
    total_patients,
    unique_conditions,
)


def test_total_patients():
    assert total_patients(patients) == 4


def test_average_age():
    # (32 + 45 + 28 + 52) / 4 == 39.25
    assert average_age(patients) == pytest.approx(39.25, abs=0.05)


def test_count_active_patients():
    assert count_active_patients(patients) == 3


def test_unique_conditions_is_sorted_and_unique():
    assert unique_conditions(patients) == ["asthma", "diabetes", "hypertension"]


def test_count_by_condition():
    assert count_by_condition(patients) == {
        "diabetes": 2,
        "hypertension": 1,
        "asthma": 1,
    }


def test_does_not_mutate_input():
    before = [dict(patient) for patient in patients]
    total_patients(patients)
    average_age(patients)
    count_active_patients(patients)
    unique_conditions(patients)
    count_by_condition(patients)
    assert patients == before
