attempts = {
    "Alice": [1, 2, 3, 4],
    "Bob": [2, 3],
    "Charlie": [1, 2, 3, 4]
}
attempt_sets = {s: set(qs) for s, qs in attempts.items()}
all_questions = set()
for qs in attempt_sets.values():
    all_questions |= qs
full_attempt_students = []
for student, qs in attempt_sets.items():
    if all_questions.issubset(qs):
        full_attempt_students.append(student)
print("Total unique questions attempted:")
print(all_questions)
print("\nStudents who attempted all questions attempted by others:")
print(full_attempt_students)