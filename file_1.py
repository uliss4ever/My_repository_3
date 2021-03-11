from typing import List
"""1277. Count Square Submatrices with All Ones"""
f = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 1, 1]]
s = []
def countSquares(f: List[List[int]]) -> int:
    for _ in range(len(f)):
        print(f[_])
    h = len(f)

    for i in range(len(f)-1):
        for j in range(len(f[0])-1):
            a = f[i][j]+f[i+1][j] +f[i][j+1] +f[i+1][j+1]
            s.append(a)
    return s
print(countSquares(f))
