passengers = [12, 25, 18, 30, 15, 20]
avg = sum(passengers) / len(passengers)
max_passengers = max(passengers)
max_stop = passengers.index(max_passengers) + 1
below_avg_stops = []
for i, count in enumerate(passengers):
    if count < avg:
        below_avg_stops.append(i + 1)
print("Stop with maximum passengers:")
print(f"Stop {max_stop} with {max_passengers} passengers")
print("\nStops with passenger count below route average:")
print(below_avg_stops)