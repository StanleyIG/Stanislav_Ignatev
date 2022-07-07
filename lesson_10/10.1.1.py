class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(str(f'|{x[0]}  {x[1]}|') for x in self.matrix)

    def __add__(self, other):
        result = [[self.matrix[i][j] + self.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))]
        return '\n'.join(f'|{i[0]}  {i[1]}|' for i in result)


m = Matrix([[12, 32], [25, 52],[78,45]])
m_1 = Matrix([[12, 32], [25, 52], [78, 47]])
print(m)
print()
print(m_1)
print()
print(m + m_1)
