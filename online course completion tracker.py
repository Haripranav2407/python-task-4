course_data = {
    "Alice": ["Module1", "Module2", "Module3"],
    "Bob": ["Module1"],
    "Charlie": ["Module1", "Module2", "Module3", "Module4"]
}
module_count = {}
for student, modules in course_data.items():
    module_count[student] = len(modules)
max_student = max(module_count, key=module_count.get)
print("Modules completed by each student:")
print(module_count)
print("\nStudent with maximum modules completed:")
print(max_student, "->", module_count[max_student])