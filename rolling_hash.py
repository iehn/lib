class ModInt():
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n+x) % mod)

    def __sub__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n-x) % mod)

    def __mul__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n*x) % mod)

    def __truediv__(self, x):
        x = ModInt.xn(x)
        return ModInt(self.n * pow(x, mod-2, mod) % mod)

    @classmethod
    def xn(cls, x):
        if isinstance(x, ModInt):
            return x.n
        return x

    def __str__(self):
        return str(self.n)

def M(n): return ModInt(n)

class RollingHash():
    def __init__(self, s):
        self.N = n = len(s)
        a = [ord(c) for c in s]
        self.A1 = a1 = [M(a[0])]
        self.A2 = a2 = [M(a[0])]
        for c in a[1:]:
            a1.append(a1[-1] * 997 + c)
            a2.append(a2[-1] * 991 + c)

    def get(self, l, r):
        if l == 0:
            return (self.A1[r].n, self.A2[r].n)
        t1 = (self.A1[r] - self.A1[l-1] * pow(997, r-l+1, mod)).n
        t2 = (self.A2[r] - self.A2[l-1] * pow(991, r-l+1, mod)).n
        return (t1, t2)
