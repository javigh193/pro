matrix = [[1, 1, 1], [1, 2, 1], [1, 3, 1]]
diagonal_sum = 0
# suponemos que es cuadrada
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]
print(diagonal_sum)
