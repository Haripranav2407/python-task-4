progress = {
    "Alice": {1, 2, 3, 4, 5},
    "Bob": {1, 2},
    "Charlie": {1, 2, 3, 4, 5},
    "David": {1}
}
all_lessons = {1, 2, 3, 4, 5}
total_lessons = len(all_lessons)
completed_all = []
less_than_half = []
for student, completed in progress.items():
    if all_lessons.issubset(completed):
        completed_all.append(student)
    if len(completed) < total_lessons / 2:
        less_than_half.append(student)
print("Students who completed all lessons:")
print(completed_all)
print("\nStudents who completed less than half of the lessons:")
print(less_than_half)