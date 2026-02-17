certifications = {
    "Alice": {"AWS", "Python", "Docker"},
    "Bob": {"AWS", "Java"},
    "Charlie": {"AWS", "Python"},
    "David": {"AWS", "Kubernetes"}
}
all_certs = set.intersection(*certifications.values())
cert_count = {}
for certs in certifications.values():
    for c in certs:
        cert_count[c] = cert_count.get(c, 0) + 1
unique_cert_employees = []
for emp, certs in certifications.items():
    if any(cert_count[c] == 1 for c in certs):
        unique_cert_employees.append(emp)
print("Certifications held by all employees:")
print(all_certs)
print("\nEmployees with unique certifications:")
print(unique_cert_employees)