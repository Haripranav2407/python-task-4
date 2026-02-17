user1_movies = ["Inception", "Avatar", "Titanic", "Interstellar"]
user2_movies = ["Avatar", "Titanic", "Joker", "Gladiator"]
set1 = set(user1_movies)
set2 = set(user2_movies)
common_movies = set1 & set2
unique_movies = set1 ^ set2
print("Common movies:", common_movies)
print("Movies watched by either one but not both:", unique_movies)