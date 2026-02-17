earnings = [
    (101, 250),
    (102, 300),
    (101, 200),
    (103, 400),
    (102, 350),
    (101, 300)
]
total_earning = {}
delivery_count = {}
for partner, amount in earnings:
    total_earning[partner] = total_earning.get(partner, 0) + amount
    delivery_count[partner] = delivery_count.get(partner, 0) + 1
average_earning = {}
for partner in total_earning:
    average_earning[partner] = total_earning[partner] / delivery_count[partner]
top_partner = max(average_earning, key=average_earning.get)
print("Total earning per partner:")
print(total_earning)
print("\nAverage earning per delivery:")
print(average_earning)
print("\nPartner with highest average earning per delivery:")
print(top_partner, "->", average_earning[top_partner])