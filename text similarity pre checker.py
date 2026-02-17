doc1 = ["data", "science", "python", "ml"]
doc2 = ["python", "ml", "ai", "data"]
set1 = set(doc1)
set2 = set(doc2)
intersection = set1 & set2
union = set1 | set2
jaccard_similarity = len(intersection) / len(union)
is_similar = jaccard_similarity >= 0.5
print("Jaccard Similarity:", jaccard_similarity)
print("Documents are similar:", is_similar)