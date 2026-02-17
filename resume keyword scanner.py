required_skills = {"Python", "SQL", "Data Structures", "OOP", "Git"}

resumes = {
    "Resume1": ["Python", "SQL", "Git", "OOP"],
    "Resume2": ["Python", "HTML", "CSS"],
    "Resume3": ["Python", "SQL", "Data Structures", "OOP", "Git"]
}
qualified_resumes = []
missing_skills = {}
for name, skills_list in resumes.items():
    skills = set(skills_list)
    matched = skills & required_skills
    match_percentage = (len(matched) / len(required_skills)) * 100
    if match_percentage >= 70:
        qualified_resumes.append(name)
    missing_skills[name] = required_skills - skills
print("Resumes matching at least 70% of required skills:")
print(qualified_resumes)
print("\nMissing skills per resume:")
print(missing_skills)