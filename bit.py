
class BIT():
    def __init__(self, n):
        i = 1
        while 2**i <= n:
            i += 1
        self.H = i
        self.N = 2**i
        self.A = [0] * self.N

    def find(self, i):
        r = 0
        while i:
            r += self.A[i]
            i -= i & (i-1) ^ i
        return r

    def update(self, i, x):
        while i < self.N:
            self.A[i] += x
            i += i & (i-1) ^ i

    def query(self, a, b):
        return self.find(b-1) - self.find(a-1)
