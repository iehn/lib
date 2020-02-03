
class Prime():
    def __init__(self, n):
        self.M = m = int(math.sqrt(n)) + 10
        self.A = a = [True] * m
        a[0] = a[1] = False
        self.T = t = [2]
        for j in range(4, m, 2):
            a[j] = False
        for i in range(3, m, 2):
            if not a[i]:
                continue
            t.append(i)
            for j in range(i*i,m,i):
                a[j] = False
        self.ds_memo = {}
        self.ds_memo[1] = set([1])

    def is_prime(self, n):
        return self.A[n]

    def division(self, n):
        d = collections.defaultdict(int)
        for c in self.T:
            while n % c == 0:
                d[c] += 1
                n //= c
            if n < 2:
                break
        if n > 1:
            d[n] += 1
        return d.items()

    # memo
    def divisions(self, n):
        if n in self.ds_memo:
            return self.ds_memo[n]

        for c in self.T:
            if n % c == 0:
                rs = set([c])
                for cc in self.divisions(n // c):
                    rs.add(cc)
                    rs.add(cc * c)
                self.ds_memo[n] = rs
                return rs

        rs = set([n])
        self.ds_memo[n] = rs
        return rs

    def sowa(self, n):
        r = 1
        for k,v in self.division(n):
            t = 1
            for i in range(1,v+1):
                t += math.pow(k, i)
            r *= t
        return r


# 速度調整版
def divisions(n):
    sq = int(math.sqrt(n)+1)
    ss = 30030
    a = [None] * (ss)
    a[0] = 1
    t = 1
    for i in range(2,ss):
        if not a[i] is None:
            continue
        if t * i > ss:
            break
        t *= i
        for j in range(i*2,ss,i):
            a[j] = 1
    a = [i for i in range(t) if a[i] is None]
    d = collections.defaultdict(int)
    for i in a[1:]:
        while n % i == 0:
            n //= i
            d[i] += 1

    for j in range(1,sq//t+2):
        if t*j > n:
            break
        for ii in a:
            i = t*j+ii
            while n % i == 0:
                n //= i
                d[i] += 1

    if n > 1:
        d[n] += 1

    r = [1]
    for k, v in d.items():
        for c in r[:]:
            for i in range(1,v+1):
                r.append(c*(k**i))

    return sorted(r)


# 約数をすべて返す
def divisions(n):
    sq = int(math.sqrt(n)+1)
    d = collections.defaultdict(int)
    while n % 2 == 0:
        n //= 2
        d[2] += 1
    i = 3
    while n > 1 and sq >= i:
        if n % i == 0:
            n //= i
            d[i] += 1
        else:
            i += 2

    if n > 1:
        d[n] += 1

    r = [1]
    for k, v in d.items():
        for c in r[:]:
            for i in range(1,v+1):
                r.append(c*(k**i))

    return sorted(r)


