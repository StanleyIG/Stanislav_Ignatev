class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('|' + '  '.join([f'{i}' for i in x]) + '|' for x in self.matrix)
        #return '\n'.join(f'{x[0]} {x[1]} {x[2]}'for x in self.matrix)


    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)


m = Matrix([[12, 32, 25], [25, 52, 30],[78,45, 25]])
m_1 = Matrix([[15, 40, 10], [35, 65, 10], [78, 47, 10]])
print(m)
print()
print(m_1)
print()
print(m + m_1)
