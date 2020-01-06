
def MF(n,d): return ModFraction(n,d)

class ModFraction():
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __add__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.d % mod
        b = xf.n * self.d % mod
        c = self.d * xf.d % mod
        return ModFraction((a+b) % mod, c)

    def __sub__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.d % mod
        b = -xf.n * self.d % mod
        c = self.d * xf.d % mod
        return ModFraction((a+b) % mod, c)

    def __mul__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.n % mod
        b = self.d * xf.d % mod
        return ModFraction(a, b)

    def __truediv__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.d % mod
        b = self.d * xf.n % mod
        return ModFraction(a, b)

    @classmethod
    def xf(cls, x):
        if isinstance(x, int):
            return ModFraction(x, 1)
        return x

    @classmethod
    def inv(cls, x):
        return pow(x, mod - 2, mod)

    def int(self):
        return self.n * ModFraction.inv(self.d) % mod

    def __str__(self):
        return "{} / {}".format(self.n, self.d)

