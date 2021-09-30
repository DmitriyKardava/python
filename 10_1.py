class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            for el in row:
                result += str(el) + '\t'
            result = result.strip() + '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError('Возможно сложение только одинаковых матриц')
        for row in range(len(self.matrix)):
            if len(self.matrix[row]) != len(other.matrix[row]):
                raise ValueError('Возможно сложение только одинаковых матриц')
        return Matrix([[a + b for a, b in zip(my_row, other_row)]
                       for my_row, other_row in zip(self.matrix, other.matrix)])


matrix1 = Matrix([[100, 200, 300],
                  [400, 500, 600],
                  [700, 800, 900]])

matrix2 = Matrix([[7, 8, 9],
                  [10, 11, 12],
                  [13, 14, 15]])

matrix3 = Matrix([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])

print(matrix1)
print(matrix2)
print(matrix3)
print(matrix1 + matrix2 + matrix3)
