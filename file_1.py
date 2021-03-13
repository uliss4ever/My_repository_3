from typing import List

"""1277. Count Square Submatrices with All Ones"""
f = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
#
#
# def is_godnyj_kvadrat(k, line, col):
#     for i in range(line, k + line): # номер строчки маленького квадратика
#         for j in range(col, k + col):  # номер столбика
#             if f[i][j] == 0:
#                 return 0
#     return 1
# def countSquares(f: List[List[int]]) -> int:
#     for _ in range(len(f)):
#         print(f[_])
#     a = 0
#     h = len(f)
#     w = len(f[0])
#     m = min(h, w)  # максимальный размер квадрата для данной матрицы
#     for k in range(1, m + 1):  # k - размер текущего квадрата
#         # count = (h - k + 1) * (w - k + 1)  # перебираем все размеры квадратов
#         count = 0
#         for i in range(h - k + 1):  # перебираем ряды
#             for j in range(w - k + 1):  # перебираем элемменты в рядах
#                 print("квадратик маленький, размер:", k, i, j)
#                 if is_godnyj_kvadrat(k, i, j) == 1:
#                     count += 1
#         print(count)
#         a += count
#     return a
# print(countSquares(f))


from typing import List
class Solution:

    def is_godnyj_kvadrat(self, matrix, k, top, left):   # селф добавила
        for i in range(top, k + top):
            for j in range(left, k + left):
                if matrix[i][j] == 0:
                    return 0
            return 1
    def countSquares(self, matrix: List[List[int]]) -> int:  # тоже
        a = 0
        h = len(matrix)
        w = len(matrix[0])
        m = min(h, w)
        for k in range(1, m + 1):
            count = 0
            for i in range(h - k + 1):
                for j in range(w - k + 1):
                    if self.is_godnyj_kvadrat(matrix, k, i, j) == 1:     # и тут
                        count += 1
            a += count
        return a

def main():   # пока не совсем ясно как это запустить
    matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
if __name__ == '__main__':


    ...