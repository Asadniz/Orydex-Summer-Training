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


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    # TODO: Define thresholds and return label.
    pass


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    # TODO: Add risk labels without modifying original records.
    pass


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    # TODO: Build and return final report.
    pass


if __name__ == "__main__":
    report = build_triage_report(patients)
    print(report)

    # TODO: Add assertions after implementing the functions.
