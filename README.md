# Collaborative Filtering

This repository contains a simple implementation of a collaborative filtering recommendation system using cosine similarity. The example demonstrates the calculation of cosine similarity between user vectors and predicts expected ratings for items.

## Features

- **Cosine Similarity Calculation:** Utilizes NumPy for efficient matrix operations to calculate cosine similarity between user vectors.
- **Expected Rating Prediction:** Predicts the expected rating for a target item using collaborative filtering.

## Usage

Explore and understand the fundamentals of collaborative filtering in recommendation systems. Use the provided code as a starting point for integrating collaborative filtering into your projects or as a learning resource.

## Input Formats

### User-Item Matrix

The collaborative filtering demo takes as input a user-item matrix representing user ratings for different items. The matrix is a two-dimensional array where rows correspond to users, and columns correspond to items.

**Example User-Item Matrix:**

```python
user_item_matrix = np.array([
    [5, 4, 2, 1, 4],
    [2, 4, 3, 4, 1],
    [2, 1, 0, 2, 3],
    [4, 5, 3, 3, 2],
    [2, 3, 0, 0, 3]
])
```

In this example, there are 5 users and 5 items. The values in the matrix represent user ratings for each item.

**Cosine Similarity Matrix**

The cosine similarity matrix is calculated based on the user-item matrix. It represents the similarity between users, computed using cosine similarity.

Example Cosine Similarity Matrix:

```python
cos_similarity_matrix = np.array([
    [1.0, 0.51, 0.29, 0.62, 0.38],
    [0.51, 1.0, 0.44, 0.71, 0.42],
    [0.29, 0.44, 1.0, 0.55, 0.16],
    [0.62, 0.71, 0.55, 1.0, 0.42],
    [0.38, 0.42, 0.16, 0.42, 1.0]
])
```

In this example, the values in the cosine similarity matrix represent the cosine similarity between pairs of users.

Target User and Item
To predict an expected rating for a specific item, you need to specify the target user and target item in the collaborative filtering calculation.

Example:

```python
target_user = 0
target_item = 0
expected_rating = calculate_expected_rating(target_user, target_item, cos_similarity_matrix, user_item_matrix)
print(expected_rating)
```

Adjust the target_user and target_item variables to predict ratings for different users and items.

### How to Run

1. Clone the repository.

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory.
   ```bash
   cd collaborative-filtering-demo
   ```
3. Run the script using a Python interpreter.
   ```bash
   python collaborative_filtering.py
   ```

# Contributors

Contributions are welcome! Feel free to open issues, suggest improvements, or contribute additional features to enhance the collaborative filtering example.
