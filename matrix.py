
class Matrix():
    def __init__(self, A):
        self.A = A
        self.row = len(A)
        self.col = len(A[0])

    def __iter__(self):
        return self.A.__iter__()

    def __getitem__(self, i):
        return self.A.__getitem__(i)

    def __add__(self, B):
        aa = self.A
        bb = B.A
        return Matrix([[aa[i][j] + bb[i][j] for j in range(self.col)] for i in range(self.row)])

    def __sub__(self, B):
        aa = self.A
        bb = B.A
        return Matrix([[aa[i][j] - bb[i][j] for j in range(self.col)] for i in range(self.row)])

    def __mul__(self, B):
        bb = [[B.A[j][i] for j in range(B.row)] for i in range(B.col)]
        return Matrix([[sum([ak * bk for ak,bk in zip(ai,bj)]) % mod for bj in bb] for ai in self.A])

    def __truediv__(self, x):
        pass

    def pow(self, n):
        A = self
        r = Matrix([[0 if j != i else 1 for j in range(self.row)] for i in range(self.row)])
        while n > 0:
            if n % 2 == 1:
                r = r * A
            A = A * A
            n //= 2
        return r

    def lu(self):
        # squarenのみ
        size = self.row
        T = copy.deepcopy(self.A)
        L = [[0]*size for _ in range(size)]
        U = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(i,size):
                L[j][i] = T[j][i]
            for j in range(i,size):
                U[i][j] = T[i][j] / T[i][i]
            for j in range(i+1,size):
                for k in range(i+1,size):
                    T[j][k] -= L[j][i] * U[i][k]

        return Matrix(L),Matrix(U)

    def __str__(self):
        return self.A.__str__()

# 連立方程式を解く
def solve_se(A, b):
    n = A.row
    L,U = A.lu()
    y = []
    for i in range(n):
        t = b[i]
        for k in range(i):
            t -= L[i][k] * y[k]
        y.append(t / L[i][i])

    x = [0] * n
    for i in range(n-1,-1,-1):
        t = y[i]
        for k in range(i+1,n):
            t -= U[i][k] * x[k]
        x[i] = t
    return x
