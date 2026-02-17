crash_reports = [
    {"app_version": "1.0", "device": "Android", "severity": "HIGH"},
    {"app_version": "1.0", "device": "iOS", "severity": "LOW"},
    {"app_version": "1.1", "device": "Android", "severity": "HIGH"},
    {"app_version": "1.1", "device": "Android", "severity": "MEDIUM"},
    {"app_version": "1.0", "device": "Android", "severity": "HIGH"}
]
high_severity_reports = []
crash_count = {}
for report in crash_reports:
    if report["severity"] == "HIGH":
        high_severity_reports.append(report)
    version = report["app_version"]
    crash_count[version] = crash_count.get(version, 0) + 1
print("High severity crash reports:")
print(high_severity_reports)
print("\nCrash count per app version:")
print(crash_count)