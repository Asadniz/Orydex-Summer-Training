"""
Automated checks for Problem 5 — p5_functions_and_lambdas.py

Spec (from task1/README.md): BMI calculation, BMI classification, name
title-casing, filtering active patients, and sorting with a lambda.
BMI categories use the standard WHO bands:
    underweight < 18.5 <= normal < 25 <= overweight < 30 <= obese
"""

import pytest

from p5_functions_and_lambdas import (
    calculate_bmi,
    classify_bmi,
    format_name,
    get_active_patients,
    patients,
    sort_patients_by_weight,
)


def test_calculate_bmi():
    # 68 / (1.65 ** 2) == 24.977...
    assert calculate_bmi(68, 1.65) == pytest.approx(24.98, abs=0.01)
    # 82 / (1.78 ** 2) == 25.880...
    assert calculate_bmi(82, 1.78) == pytest.approx(25.88, abs=0.01)


def test_classify_bmi_bands():
    assert classify_bmi(17.0) == "underweight"
    assert classify_bmi(22.0) == "normal"
    assert classify_bmi(27.0) == "overweight"
    assert classify_bmi(32.0) == "obese"


def test_format_name():
    assert format_name("ayesha khan") == "Ayesha Khan"
    assert format_name("OMAR ALI") == "Omar Ali"


def test_get_active_patients():
    active = get_active_patients(patients)
    assert [patient["name"] for patient in active] == ["ayesha khan", "sara ahmed"]


def test_sort_patients_by_weight():
    ordered = sort_patients_by_weight(patients)
    assert [patient["weight_kg"] for patient in ordered] == [54, 68, 82]
