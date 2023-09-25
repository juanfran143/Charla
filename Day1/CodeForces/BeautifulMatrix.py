# https://codeforces.com/problemset/problem/263/A

def min_moves_to_beautiful_matrix(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                return abs(i - 2) + abs(j - 2)

# Test with an example matrix
example_matrix = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
min_moves_to_beautiful_matrix(example_matrix)
