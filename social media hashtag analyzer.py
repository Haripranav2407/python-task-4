posts = [
    ["#python", "#coding", "#fun"],
    ["#python", "#coding", "#learning"],
    ["#python", "#coding"]
]
post_sets = [set(post) for post in posts]
all_hashtags = set()
for s in post_sets:
    all_hashtags |= s
common_hashtags = post_sets[0].copy()
for s in post_sets[1:]:
    common_hashtags &= s
print("All unique hashtags:")
print(all_hashtags)
print("\nHashtags used in every post:")
print(common_hashtags)