quiz_scores = {
    "Alice": [80, 85, 90],
    "Bob": [70, 75, 72],
    "Charlie": [88, 92, 91]
}
student_avg = {}
total_sum = 0
total_count = 0
for student, scores in quiz_scores.items():
    avg = sum(scores) / len(scores)
    student_avg[student] = avg
    total_sum += sum(scores)
    total_count += len(scores)
class_avg = total_sum / total_count
above_avg_students = []
for student, avg in student_avg.items():
    if avg > class_avg:
        above_avg_students.append(student)
print("Average score per student:")
print(student_avg)
print("\nClass average:")
print(class_avg)
print("\nStudents above class average:")
print(above_avg_students)