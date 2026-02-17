readings = [
    {"id": 1, "temp": 30, "humidity": 60},
    {"id": 2, "temp": 31, "humidity": 58},
    {"id": 3, "temp": 29},                 # faulty
    {"id": 4, "temp": 32, "humidity": 61, "pressure": 101}  # faulty
]
expected_keys = set(readings[0].keys())
faulty_readings = []
for reading in readings:
    if set(reading.keys()) != expected_keys:
        faulty_readings.append(reading)
all_valid = len(faulty_readings) == 0

print("All readings have same keys:", all_valid)
print("\nFaulty readings:")
print(faulty_readings)