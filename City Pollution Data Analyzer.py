aqi_data = {
    "Delhi": [220, 210, 230, 240],
    "Mumbai": [150, 160, 155, 145],
    "Chennai": [120, 130, 125, 128]
}
avg_aqi = {}
for city, values in aqi_data.items():
    avg_aqi[city] = sum(values) / len(values)
worst_city = max(avg_aqi, key=avg_aqi.get)
print("Average AQI per city:")
print(avg_aqi)
print("\nCity with worst average air quality:")
print(worst_city, "->", avg_aqi[worst_city])
