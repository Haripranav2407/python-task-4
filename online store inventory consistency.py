inventory = [
    {"product_id": "P1", "category": "Electronics", "stock": 10},
    {"product_id": "P2", "category": "Electronics", "stock": 0},
    {"product_id": "P3", "category": "Clothing", "stock": 5},
    {"product_id": "P4", "category": "Clothing", "stock": 0},
    {"product_id": "P5", "category": "Books", "stock": 12}
]
all_in_stock = True
for product in inventory:
    if product["stock"] <= 0:
        all_in_stock = False
        break
out_of_stock_categories = set()
for product in inventory:
    if product["stock"] == 0:
        out_of_stock_categories.add(product["category"])
print("All products have stock greater than zero:")
print(all_in_stock)
print("\nCategories with out-of-stock products:")
print(out_of_stock_categories)