import math
import numpy as np


def cosine_similarity(user1, user2):
    dot_product = np.dot(user1, user2)
    norm_user1 = np.linalg.norm(user1)
    norm_user2 = np.linalg.norm(user2)

    similarity = dot_product / \
        (norm_user1 * norm_user2) if norm_user1 * norm_user2 != 0 else 0
    return round(similarity, 2)


def calculate_expected_ratings(target_user, cos_similarity_matrix, user_item_matrix):
    expected_ratings = []

    for target_item in range(user_item_matrix.shape[1]):
        numerator = 0
        denominator = sum(cos_similarity_matrix[target_user][1:])

        for neighbor_user in range(1, len(cos_similarity_matrix)):
            similarity = cos_similarity_matrix[target_user][neighbor_user]
            rating = user_item_matrix[neighbor_user][target_item]
            numerator += similarity * rating

        expected_rating = numerator / denominator if denominator != 0 else 0
        expected_ratings.append(round(expected_rating, 2))

    return expected_ratings


users = 5
items = 5
user_item_matrix = np.array([[5, 4, 2, 1, 4], [2, 4, 3, 4, 1], [
                            2, 1, 0, 2, 3], [4, 5, 3, 3, 2], [2, 3, 0, 0, 3]])

cos_similarity_matrix = np.zeros((users, users))
for i in range(users):
    for j in range(users):
        cos_similarity_matrix[i][j] = cosine_similarity(
            user_item_matrix[i], user_item_matrix[j])

print("Cosine Similarity Matrix:")
print(cos_similarity_matrix)

target_user = 0
expected_ratings = calculate_expected_ratings(
    target_user, cos_similarity_matrix, user_item_matrix)
print(f"Expected Ratings for User {target_user}:", expected_ratings)

# This part is to show how to use the above functions to recommend items to a user
# You can replace the target_user with any other user to get recommendations for them

recommended_items = []
for item in range(items):
    if expected_ratings[item] > 3:
        recommended_items.append(item + 1)

print(f"Recommended Items for User {target_user}:", recommended_items)

# This part is to show how to get the top N items with the highest expected ratings
top_n_items = 3
sorted_expected_ratings = sorted(
    enumerate(expected_ratings), key=lambda x: x[1], reverse=True)
top_n_recommended_items = [item + 1 for item,
                           _ in sorted_expected_ratings[:top_n_items]]

print(f"Top {top_n_items} Recommended Items for User {target_user}:",
      top_n_recommended_items)
