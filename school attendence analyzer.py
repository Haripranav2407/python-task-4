attendance = {
    "Alice": {"Mon", "Tue", "Wed", "Thu", "Fri"},
    "Bob": {"Mon", "Wed", "Thu"},
    "Charlie": {"Mon", "Tue", "Wed", "Thu", "Fri"}
}
working_days = {"Mon", "Tue", "Wed", "Thu", "Fri"}
total_days = {}
for student, days in attendance.items():
    total_days[student] = len(days)
full_attendance = []
for student, days in attendance.items():
    if working_days.issubset(days):
        full_attendance.append(student)
print("Total attendance days per student:")
print(total_days)
print("\nStudents who attended on all working days:")
print(full_attendance)