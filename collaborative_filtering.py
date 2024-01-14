import math
import numpy as np


def cosine_similarity(user1, user2):
    dot_product = np.dot(user1, user2)
    norm_user1 = np.linalg.norm(user1)
    norm_user2 = np.linalg.norm(user2)

    similarity = dot_product / \
        (norm_user1 * norm_user2) if norm_user1 * norm_user2 != 0 else 0
    return round(similarity, 2)


def calculate_expected_rating(target_user, target_item, cos_similarity_matrix, user_item_matrix):
    numerator = 0
    denominator = sum(cos_similarity_matrix[target_user][1:])

    for neighbor_user in range(1, len(cos_similarity_matrix)):
        similarity = cos_similarity_matrix[target_user][neighbor_user]
        rating = user_item_matrix[neighbor_user][target_item]
        numerator += similarity * rating

    expected_rating = numerator / denominator if denominator != 0 else 0
    return round(expected_rating, 2)


users = 5
items = 5
user_item_matrix = np.array([[5, 4, 2, 1, 4], [2, 4, 3, 4, 1], [
                            2, 1, 0, 2, 3], [4, 5, 3, 3, 2], [2, 3, 0, 0, 3]])

cos_similarity_matrix = np.zeros((users, users))
for i in range(users):
    for j in range(users):
        cos_similarity_matrix[i][j] = cosine_similarity(
            user_item_matrix[i], user_item_matrix[j])

print(cos_similarity_matrix)

target_user = 0
target_item = 0
expected_rating = calculate_expected_rating(
    target_user, target_item, cos_similarity_matrix, user_item_matrix)
print(expected_rating)
