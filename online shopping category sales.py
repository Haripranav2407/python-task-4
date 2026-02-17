sales = {
    "Electronics": [12000, 8000, 15000],
    "Clothing": [3000, 4500, 2500],
    "Books": [1200, 800, 600]
}
total_sales = {}
for category, amounts in sales.items():
    total_sales[category] = sum(amounts)
top_category = max(total_sales, key=total_sales.get)
print("Total sales per category:")
print(total_sales)
print("\nCategory with highest total revenue:")
print(top_category, "->", total_sales[top_category])