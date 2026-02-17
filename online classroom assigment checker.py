submissions = {
    "Alice": [1, 2, 3],
    "Bob": [2, 3],
    "Charlie": [1, 2, 3]
}
all_assignments = {1, 2, 3, 4}
submission_sets = {s: set(a) for s, a in submissions.items()}
full_submitters = []
for student, submitted in submission_sets.items():
    if all_assignments.issubset(submitted):
        full_submitters.append(student)
submitted_any = set()
for submitted in submission_sets.values():
    submitted_any |= submitted
not_submitted = all_assignments - submitted_any
print("Students who submitted all assignments:")
print(full_submitters)
print("\nAssignments not submitted by any student:")
print(not_submitted)