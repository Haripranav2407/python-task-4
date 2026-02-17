visits = [
    {"patient_id": "P1", "doctor": "Dr.A", "visit_count": 3},
    {"patient_id": "P2", "doctor": "Dr.B", "visit_count": 5},
    {"patient_id": "P3", "doctor": "Dr.A", "visit_count": 2},
    {"patient_id": "P4", "doctor": "Dr.C", "visit_count": 4},
    {"patient_id": "P5", "doctor": "Dr.B", "visit_count": 1}
]
doctor_visits = {}
max_patient = None
max_visits = 0
for record in visits:
    patient = record["patient_id"]
    doctor = record["doctor"]
    count = record["visit_count"]
    doctor_visits[doctor] = doctor_visits.get(doctor, 0) + count
    if count > max_visits:
        max_visits = count
        max_patient = patient
print("Doctor-wise total visits:")
print(doctor_visits)
print("\nPatient with highest visit count:")
print(max_patient, "->", max_visits)