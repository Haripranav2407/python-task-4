logs = [
    (101, "09:00"),
    (102, "09:05"),
    (101, "09:00"),
    (103, "09:10"),
    (102, "09:05"),
    (101, "09:15")
]
seen = set()
invalid_logs = []
for entry in logs:
    if entry in seen:
        invalid_logs.append(entry)
    else:
        seen.add(entry)
print("Invalid log entries:")
print(invalid_logs)