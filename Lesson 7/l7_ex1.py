'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.'''


class Matrix:
    def __init__(self, m):
        self.m = m

    def __str__(self):
        my_str = ''
        for el in self.m:
            my_str = my_str + str(el) + '\n'
        return my_str

    def my_len(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        m, n = self.my_len()
        my_sum = Matrix([[0 for x in range(n)] for y in range(m)])
        if isinstance(other, Matrix):
            if (m, n) != other.my_len():
                print('only same size matrices can be added')
            else:
                for i in range(0, m):
                    for j in range(0, n):
                        my_sum.m[i][j] = (self.m[i][j] + other.m[i][j])
                return my_sum
        else:
            print('only matrices can be added')


my_data = [[1, 2],
           [4, 5],
           [7, 8]]

your_data = [[2, 3],
             [5, 6],
             [8, 9]]

matrix_1 = Matrix(my_data)
matrix_2 = Matrix(your_data)

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
