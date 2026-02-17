documents = [
    {"doc_id": 1, "tags": ["python", "ai", "ml"]},
    {"doc_id": 2, "tags": ["python", "ai"]},
    {"doc_id": 3, "tags": ["python", "ai", "data"]}
]
all_have_tags = True
for doc in documents:
    if not doc["tags"]:
        all_have_tags = False
        break
tag_sets = [set(doc["tags"]) for doc in documents]
common_tags = tag_sets[0].copy()
for s in tag_sets[1:]:
    common_tags &= s
print("All documents have at least one tag:")
print(all_have_tags)
print("\nTags that appear in every document:")
print(common_tags)