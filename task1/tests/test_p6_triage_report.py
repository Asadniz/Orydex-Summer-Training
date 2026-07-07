"""
Automated checks for Problem 6 — p6_triage_report.py

Spec is derived from the Day 1 fast-track notebook
(python_standards_fast_track.ipynb), adapted to the integer 0-100
risk-score scale used in p6_triage_report.py:

    risk_score >= 75            -> "high"
    50 <= risk_score < 75       -> "medium"
    risk_score < 50             -> "low"

The notebook uses the float 0.0-1.0 scale (0.75 / 0.50); these are the
same thresholds scaled by 100.
"""

import copy

from p6_triage_report import (
    add_risk_labels,
    build_triage_report,
    label_risk,
    patients,
)

HIGH_THRESHOLD = 75
MEDIUM_THRESHOLD = 50
VALID_LABELS = {"low", "medium", "high"}
RISK_RANK = {"low": 0, "medium": 1, "high": 2}


# --------------------------------------------------------------------------- #
# label_risk
# --------------------------------------------------------------------------- #
def test_label_risk_high():
    assert label_risk(75) == "high"
    assert label_risk(88) == "high"
    assert label_risk(100) == "high"


def test_label_risk_medium():
    assert label_risk(50) == "medium"
    assert label_risk(72) == "medium"
    assert label_risk(74) == "medium"


def test_label_risk_low():
    assert label_risk(0) == "low"
    assert label_risk(35) == "low"
    assert label_risk(49) == "low"


def test_label_risk_boundaries():
    """Bands are inclusive on the lower edge."""
    assert label_risk(MEDIUM_THRESHOLD - 1) == "low"
    assert label_risk(MEDIUM_THRESHOLD) == "medium"
    assert label_risk(HIGH_THRESHOLD - 1) == "medium"
    assert label_risk(HIGH_THRESHOLD) == "high"


def test_label_risk_returns_valid_label():
    for score in range(0, 101):
        assert label_risk(score) in VALID_LABELS


def test_label_risk_is_monotonic():
    """A higher score must never produce a lower-risk label."""
    previous = -1
    for score in range(0, 101):
        rank = RISK_RANK[label_risk(score)]
        assert rank >= previous, f"label_risk dropped at score {score}"
        previous = rank


# --------------------------------------------------------------------------- #
# add_risk_labels
# --------------------------------------------------------------------------- #
def test_add_risk_labels_adds_label_field():
    labelled = add_risk_labels(patients)
    assert all("risk_label" in patient for patient in labelled)


def test_add_risk_labels_label_matches_label_risk():
    labelled = add_risk_labels(patients)
    for patient in labelled:
        assert patient["risk_label"] == label_risk(patient["risk_score"])


def test_add_risk_labels_preserves_original_fields():
    labelled = add_risk_labels(patients)
    assert len(labelled) == len(patients)
    for original, result in zip(patients, labelled):
        for key, value in original.items():
            assert result[key] == value


def test_add_risk_labels_does_not_mutate_input():
    snapshot = copy.deepcopy(patients)
    add_risk_labels(patients)
    assert patients == snapshot, "add_risk_labels must not modify the originals"
    assert all("risk_label" not in patient for patient in patients)


def test_add_risk_labels_returns_new_objects():
    labelled = add_risk_labels(patients)
    for original, result in zip(patients, labelled):
        assert result is not original, "return copies, not the same dict objects"


# --------------------------------------------------------------------------- #
# build_triage_report
# --------------------------------------------------------------------------- #
def test_report_has_expected_keys():
    report = build_triage_report(patients)
    assert set(report.keys()) == {
        "summary",
        "risk_counts",
        "active_high_risk_patients",
    }


def test_report_summary_total_patients():
    report = build_triage_report(patients)
    assert report["summary"]["total_patients"] == len(patients)


def test_report_risk_counts_sum_to_total():
    report = build_triage_report(patients)
    assert sum(report["risk_counts"].values()) == len(patients)


def test_report_risk_counts_values_for_sample_data():
    # Sample scores: 72 -> medium, 88 -> high, 35 -> low, 91 -> high
    report = build_triage_report(patients)
    counts = report["risk_counts"]
    assert counts.get("high", 0) == 2
    assert counts.get("medium", 0) == 1
    assert counts.get("low", 0) == 1


def test_report_active_high_risk_count():
    report = build_triage_report(patients)
    assert len(report["active_high_risk_patients"]) == 2


def test_report_active_high_risk_are_active_and_high():
    report = build_triage_report(patients)
    for patient in report["active_high_risk_patients"]:
        assert patient["active"] is True
        assert patient["risk_label"] == "high"


def test_report_active_high_risk_identities():
    report = build_triage_report(patients)
    ids = {patient["id"] for patient in report["active_high_risk_patients"]}
    assert ids == {2, 4}  # Omar Ali (88) and Bilal Malik (91)


def test_report_handles_empty_input():
    report = build_triage_report([])
    assert report["summary"]["total_patients"] == 0
    assert sum(report["risk_counts"].values()) == 0
    assert report["active_high_risk_patients"] == []
