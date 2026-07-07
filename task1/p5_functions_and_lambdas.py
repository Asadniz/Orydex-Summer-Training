"""
Task 1 — Functions and Lambda Functions

Practice reusable functions, type hints, and lambda functions.
Complete this file without using AI tools.
"""

patients = [
    {"name": "ayesha khan", "height_m": 1.65, "weight_kg": 68, "active": True},
    {"name": "omar ali", "height_m": 1.78, "weight_kg": 82, "active": False},
    {"name": "sara ahmed", "height_m": 1.60, "weight_kg": 54, "active": True},
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    # TODO: Implement BMI formula.
    pass


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    # TODO: Return underweight, normal, overweight, or obese.
    pass


def format_name(name: str) -> str:
    """Convert a name to title case."""
    # TODO: Format name.
    pass


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    # TODO: Filter active patients.
    pass


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    # TODO: Sort patients by weight_kg.
    pass


if __name__ == "__main__":
    # TODO: Call your functions and print useful output.
    pass
