employee_skills = {
    "Alice": {"Python", "SQL", "Java"},
    "Bob": {"Python", "C++"},
    "Charlie": {"Python", "SQL", "C"}
}
both_python_sql = []
for emp, skills in employee_skills.items():
    if {"Python", "SQL"}.issubset(skills):
        both_python_sql.append(emp)
all_skills = set()
for skills in employee_skills.values():
    all_skills |= skills
common_skills = None
for skills in employee_skills.values():
    if common_skills is None:
        common_skills = skills.copy()
    else:
        common_skills &= skills
print("Employees who know both Python and SQL:")
print(both_python_sql)
print("\nSkills known by at least one employee:")
print(all_skills)
print("\nSkills known by all employees:")
print(common_skills)