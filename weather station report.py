temps = [
    [30, 32, 31, 29, 28, 30, 31],
    [33, 34, 35, 36, 34, 33, 32],
    [25, 26, 27, 26, 25, 24, 23]
]
weekly_avg = []
hottest = temps[0][0]
for week in temps:
    avg = sum(week) / len(week)
    weekly_avg.append(avg)
    for t in week:
        if t > hottest:
            hottest = t
max_avg_week = weekly_avg.index(max(weekly_avg)) + 1
print("Average temperature per week:")
print(weekly_avg)
print("\nHottest temperature overall:")
print(hottest)
print("\nWeek with highest average temperature:")
print(max_avg_week)