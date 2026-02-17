traffic = [
    [120, 150, 180, 200],
    [100, 130, 160, 170],
    [140, 160, 190, 210]
]
junction_totals = [sum(row) for row in traffic]
max_junction = junction_totals.index(max(junction_totals)) + 1
hours = len(traffic[0])
hour_totals = []
for h in range(hours):
    total = 0
    for j in range(len(traffic)):
        total += traffic[j][h]
    hour_totals.append(total)
max_hour = hour_totals.index(max(hour_totals)) + 1
print("Junction with highest total traffic:")
print(f"Junction {max_junction} -> {junction_totals[max_junction-1]} vehicles")
print("\nHour with highest traffic across all junctions:")
print(f"Hour {max_hour} -> {hour_totals[max_hour-1]} vehicles")