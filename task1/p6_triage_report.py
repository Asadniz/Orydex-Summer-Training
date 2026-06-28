"""
Task 1 — Final Problem: Triage Report

Complete this file without using AI tools.
Use fake/sample data only.

Tip: collections.Counter can make counting by risk label easier, but a
plain dictionary works too — import it yourself if you want to use it.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]

from helper import b_sort


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    # TODO: Define thresholds and return label.
    if risk_score < 50:
        return "low"
    if risk_score >= 50 and risk_score < 75:
        return "medium"
    if risk_score >= 75:
        return "high"


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    # TODO: Add risk labels without modifying original records.
    patient_records_copy = [None] * len(patient_records)
    for i in range (len(patient_records)):
        patient_records_copy[i] = dict(patient_records[i])
            
    for patient in patient_records_copy:
        patient["risk_label"] = label_risk(patient["risk_score"])
    return patient_records_copy


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    # TODO: Build and return final report.
    report = {"summary": {}, "risk_counts": {"low": 0, "medium": 0, "high": 0}, "active_high_risk_patients": []}

    report["summary"]["total_patients"] = len(patient_records)
    risk_labelled_report = add_risk_labels(patient_records)

    for i in range (len(risk_labelled_report)):
        risk_label = risk_labelled_report[i]["risk_label"]
        report["risk_counts"][risk_label] += 1
        if risk_label == "high" and risk_labelled_report[i]["active"]:
            report["active_high_risk_patients"].append (risk_labelled_report[i])

    return report


if __name__ == "__main__":
    report = build_triage_report(patients)
    print(report)

    # TODO: Add assertions after implementing the functions.
