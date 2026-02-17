exam_slots = [
    ("Alice", 101),
    ("Bob", 102),
    ("Charlie", 103),
    ("Alice", 104),
    ("David", 102)
]
students_seen = set()
slots_seen = set()
invalid = []
for student, slot in exam_slots:
    if student in students_seen or slot in slots_seen:
        invalid.append((student, slot))
    else:
        students_seen.add(student)
        slots_seen.add(slot)
if invalid:
    print("Invalid assignments:")
    for entry in invalid:
        print(entry)
else:
    print("All assignments are valid")
