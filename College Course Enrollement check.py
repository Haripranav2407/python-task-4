enrollments = {
    "Math": {101, 102, 103, 104},
    "Physics": {103, 104, 105},
    "Chemistry": {102, 106}
}
student_count = {}
for students in enrollments.values():
    for s in students:
        student_count[s] = student_count.get(s, 0) + 1
multi_course_students = [s for s, c in student_count.items() if c > 1]
course_sizes = {course: len(students) for course, students in enrollments.items()}
max_enrollment = max(course_sizes.values())
max_courses = [course for course, size in course_sizes.items() if size == max_enrollment]
print("Students enrolled in more than one course:")
print(multi_course_students)
print("\nCourses with maximum enrollment:")
print(max_courses, "->", max_enrollment)