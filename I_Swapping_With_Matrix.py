def swap_matrix(matrix, x, y):
    # Swap rows
    matrix[x], matrix[y] = matrix[y], matrix[x]

    # Swap columns
    for i in range(len(matrix)):
        matrix[i][x], matrix[i][y] = matrix[i][y], matrix[i][x]

    return matrix


N, X, Y = map(int, input().split())
X -= 1
Y -= 1

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

swap_matrix(matrix, X, Y)

for row in matrix:
    print(*row)  
