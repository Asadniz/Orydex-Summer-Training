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

from helper import b_sort

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    # TODO: Implement BMI formula.
    return weight_kg / ((height_m) ** 2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    # TODO: Return underweight, normal, overweight, or obese.
    if bmi < 18.5:
        return "underweight"
    if bmi >= 18.5 and bmi < 25:
        return "normal"
    if bmi >= 25 and bmi < 30:
        return "overweight"
    if bmi >= 30:
        return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    # TODO: Format name.
    formatted_name = ""
    capital_flag = True

    for character in name:
        ascii_value = ord(character)
        
        if ascii_value == 32:
            formatted_name += character
            capital_flag = True
            continue

        if ascii_value < 65 or ascii_value > 122 or (ascii_value > 90 and ascii_value < 97):
            print (ascii_value)
            return "INVALID NAME"
        
        if capital_flag:
            if ascii_value > 90:
                ascii_value -= 32
            capital_flag = False

        else:
            if ascii_value < 97:
                ascii_value += 32
        formatted_name += chr(ascii_value)

    return formatted_name
    


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    # TODO: Filter active patients.
    return [patient for patient in patient_records if patient["active"] == True]
    


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    # TODO: Sort patients by weight_kg.
    lst = patient_records.copy()
    b_sort(lst, key = lambda x : x["weight_kg"])
    return lst


if __name__ == "__main__":
    # TODO: Call your functions and print useful output.
    patient = patients[0]
    bmi = calculate_bmi(patient["weight_kg"], patient["height_m"])
    classification = classify_bmi(bmi)
    active_patients = get_active_patients(patients)
    weight_sorted = sort_patients_by_weight(patients)
    print ("----------")
    print ("BMI: ", bmi)
    print ("BMI Range: ", classification)
    print ("Active Patients: ", active_patients)
    print ("Patients by Weight: ", weight_sorted)
    print ("----------")
