students = [
    {"name": "Alice", "dept": "CSE", "cgpa": 8.5},
    {"name": "Bob", "dept": "ECE", "cgpa": 7.8},
    {"name": "Charlie", "dept": "CSE", "cgpa": 9.0},
    {"name": "David", "dept": "ECE", "cgpa": 8.2},
    {"name": "Eva", "dept": "ME", "cgpa": 7.5}
]
dept_total = {}
dept_count = {}
for student in students:
    dept = student["dept"]
    cgpa = student["cgpa"]
    dept_total[dept] = dept_total.get(dept, 0) + cgpa
    dept_count[dept] = dept_count.get(dept, 0) + 1
dept_avg = {}
for dept in dept_total:
    dept_avg[dept] = dept_total[dept] / dept_count[dept]
print(dept_avg)