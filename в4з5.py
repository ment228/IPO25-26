import numpy as np

# Создаем массив A размером 5x2
A = np.array([[1, 6], [2, 8], [3, 11], [3, 9], [1, 7]])
print("Матрица A:\n", A)

# Получаем матрицу AT путем транспонирования матрицы A
AT = A.T
print("Транспонированная матрица AT:\n", AT)
