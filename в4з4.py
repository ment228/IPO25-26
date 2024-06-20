import numpy as np

# Создаем одномерный массив A из последовательности целых чисел от 0 до 11
A = np.arange(12)
print("Одномерный массив A: ", A)

# Меняем форму этого массива для получения матрицы C, состоящей из четырех строк и трех столбцов
C = A.reshape(4, 3)
print("Матрица C:\n", C)

# Получаем матрицу CT путем транспонирования матрицы C
CT = C.T
print("Транспонированная матрица CT:\n", CT)

# Получаем матрицу B, умножив матрицу C на CT с помощью матричного умножения
B = np.dot(C, CT)
print("Матрица B:\n", B)
