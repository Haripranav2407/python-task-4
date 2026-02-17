usage_logs = {
    "D1": [2, 3, 1, 4],
    "D2": [1, 1, 2],
    "D3": [4, 5, 3],
    "D4": [2]
}
total_usage = {}
for device, hours in usage_logs.items():
    total_usage[device] = sum(hours)
average_usage = sum(total_usage.values()) / len(total_usage)
above_average_devices = [
    device for device, total in total_usage.items()
    if total > average_usage
]
print("Total usage hours per device:")
print(total_usage)
print("\nAverage usage across all devices:")
print(average_usage)
print("\nDevices with usage above average:")
print(above_average_devices)