"""
Task 1 — Dictionary Analysis

Practice dictionaries and nested dictionaries.
Complete this file without using AI tools.
"""

patients = {
    1: {
        "name": "Ayesha Khan",
        "age": 32,
        "contact": {"city": "Karachi", "phone": "000-000"},
        "condition": "diabetes",
    },
    2: {
        "name": "Omar Ali",
        "age": 45,
        "contact": {"city": "Lahore", "phone": "111-111"},
        "condition": "hypertension",
    },
}


def get_patient_city(patient_id):
    """Return the city for a given patient ID."""
    # TODO: Safely return the city.
    if patient_id in patients.keys():
        city = (patients[patient_id]).get("contact")["city"]
        print ("Registered city for Patient ID ", patient_id, " is ", city)
        return city
    print("ERROR: ID not found")


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    # TODO: Update the condition for the patient.
    temp = patients[patient_id].get("condition")
    (patients[patient_id])["condition"] = new_condition
    print("Updated condition of patient with id ", patient_id, " from ", temp, " to ", new_condition)


def build_patient_summary():
    """Build and return a summary dictionary."""
    # TODO: Return useful summary information.
    summary = patients.copy()
    summary["total_patients"] = len(patients)
    return summary


if __name__ == "__main__":
    # TODO: Call your functions and print results.
    print(get_patient_city(1), "\n")
    print(update_patient_condition(1, "asthma"), "\n")
    print(build_patient_summary(), "\n")
