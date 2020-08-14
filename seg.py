
class Seg():
    def __init__(self, na, default, func):
        if isinstance(na, list):
            n = len(na)
        else:
            n = na
        i = 1
        while 2**i <= n:
            i += 1
        self.D = default
        self.H = i
        self.N = 2**i
        if isinstance(na, list):
            self.A = [default] * (self.N) + na + [default] * (self.N-n)
            for i in range(self.N-1,0,-1):
                self.A[i] = func(self.A[i*2], self.A[i*2+1])
        else:
            self.A = [default] * (self.N*2)
        self.F = func

    def find(self, i):
        return self.A[i + self.N]

    def update(self, i, x):
        i += self.N
        self.A[i] = x
        while i > 1:
            i = i // 2
            self.A[i] = self.merge(self.A[i*2], self.A[i*2+1])

    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[1]

    def query(self, a, b):
        A = self.A
        l = a + self.N
        r = b + self.N
        res = self.D
        while l < r:
            if l % 2 == 1:
                res = self.merge(res, A[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.merge(res, A[r])
            l >>= 1
            r >>= 1

        return res


class RangeAddSum():
    def __init__(self, n):
        i = 1
        while 2**i <= n:
            i += 1
        self.N = 2**i
        self.A = [0] * (self.N*2)
        self.B = [0] * (self.N*2)

    def add(self, a, b, x, k, l, r):
        def ina(k, l, r):
            if a <= l and r <= b:
                self.A[k] += x
            elif l < b and a < r:
                self.B[k] += (min(b, r) - max(a, l)) * x
                m = (l+r) // 2
                ina(k*2+1, l, m)
                ina(k*2+2, m, r)

        ina(k, l, r)

    def query(self, a, b, k, l, r):
        def inq(k, l, r):
            if b <= l or r <= a:
                return 0

            if a <= l and r <= b:
                return self.A[k] * (r - l) + self.B[k]

            res = (min(b, r) - max(a, l)) * self.A[k]
            m = (l+r) // 2
            res += inq(k*2+1, l, m)
            res += inq(k*2+2, m, r)
            return res

        return inq(k, l, r)


# maxへの変更も単純にできる, Starry Sky Tree(?)
class RangeAddMin():
    def __init__(self, n):
        i = 1
        while 2**i <= n:
            i += 1
        self.N = 2**i
        self.A = [0] * (self.N*2)
        self.B = [0] * (self.N*2)

    def add(self, a, b, x, k, l, r):
        def ina(k, l, r):
            if b <= l or r <= a:
                pass
            elif a <= l and r <= b:
                self.A[k] += x
            else:
                m = (l+r) // 2
                ina(k*2+1, l, m)
                ina(k*2+2, m, r)
                self.B[k] = min(self.B[k*2+1] + self.A[k*2+1], self.B[k*2+2] + self.A[k*2+2])

        ina(k, l, r)

    def query(self, a, b, k, l, r):
        def inq(k, l, r):
            if b <= l or r <= a:
                return inf

            if a <= l and r <= b:
                return self.A[k] + self.B[k]

            m = (l+r) // 2
            rl = inq(k*2+1, l, m)
            rr = inq(k*2+2, m, r)
            return min(rl, rr) + self.A[k]

        return inq(k, l, r)
