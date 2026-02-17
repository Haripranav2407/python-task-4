delays = {
    "AI101": [10, 20, 0, 15],
    "AI202": [30, 25],
    "AI303": [5, 0, 10]
}
avg_delay = {}
for flight, mins in delays.items():
    avg_delay[flight] = sum(mins) / len(mins)
worst_flight = max(avg_delay, key=avg_delay.get)
print("Average delay per flight:")
print(avg_delay)
print("\nFlight with highest average delay:")
print(worst_flight, "->", avg_delay[worst_flight])