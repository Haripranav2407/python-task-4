usage = {
    "U1": [1.2, 1.5, 1.0, 2.0],
    "U2": [0.8, 0.9, 1.1],
    "U3": [2.5, 2.0, 2.8]
}
limit = 5.0
total_usage = {}
avg_usage = {}
for user, data in usage.items():
    total = sum(data)
    avg = total / len(data)
    total_usage[user] = total
    avg_usage[user] = avg
exceeded_users = [u for u, t in total_usage.items() if t > limit]
top_user = max(avg_usage, key=avg_usage.get)
print("Users whose total usage exceeded the limit:")
print(exceeded_users)
print("\nUser with highest average daily usage:")
print(top_user, "->", avg_usage[top_user])