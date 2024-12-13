###5
def find_rows_with_extreme_sums(matrix):
    max_sum_index = 0
    min_sum_index = 0
    max_sum = sum(matrix[0])
    min_sum = sum(matrix[0])

    for i in range(1, len(matrix)):
        current_sum = sum(matrix[i])
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_index = i
            
        if current_sum < min_sum:
            min_sum = current_sum
            min_sum_index = i

    return matrix[max_sum_index], max_sum, matrix[min_sum_index], min_sum

# Пример использования
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 1, 1]
]

max_row, max_row_sum, min_row, min_row_sum = find_rows_with_extreme_sums(matrix)

print("Строка с наибольшей суммой элементов:", max_row, "Сумма:", max_row_sum)
print("Строка с наименьшей суммой элементов:", min_row, "Сумма:", min_row_sum)


###6
import numpy as np

def transform_matrix(matrix):
    new_matrix = []
    
    for row in matrix:
        min_value = min(row)
        if min_value % 2 == 0:
            new_matrix.append([0] * len(row))
        else:
            new_matrix.append([1] * len(row))
    
    return new_matrix

# Пример использования
matrix = [
    [3.5, 2.1, 4.7],
    [1.2, 5.6, 0.9],
    [7.3, 8.4, 6.2]
]

new_matrix = transform_matrix(matrix)

print("Новая матрица:")
for row in new_matrix:
    print(row)
