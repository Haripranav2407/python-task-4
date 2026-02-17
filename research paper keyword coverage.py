papers = {
    "P1": ["AI", "ML", "Data", "Python"],
    "P2": ["AI", "Data", "Statistics"],
    "P3": ["AI", "ML", "Data", "DeepLearning"]
}
paper_sets = {p: set(k) for p, k in papers.items()}
all_keywords = set()
for kws in paper_sets.values():
    all_keywords |= kws
common_keywords = None
for kws in paper_sets.values():
    if common_keywords is None:
        common_keywords = kws.copy()
    else:
        common_keywords &= kws
max_paper = max(paper_sets, key=lambda p: len(paper_sets[p]))
print("Total unique keywords across all papers:")
print(all_keywords)
print("\nKeywords common to every paper:")
print(common_keywords)
print("\nPaper with maximum number of unique keywords:")
print(max_paper, "->", len(paper_sets[max_paper]))