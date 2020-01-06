import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7



class SquareDecomposition():

    def __init__(self, mi, ma):
        self.min = mi
        self.max = ma
        n = ma - mi + 1
        self.N = n
        self.a = [0] * n
        self.sq = int(math.sqrt(n))
        self.sqa = [0] * (self.sq+1)

    def add(self, x):
        xi = x - self.min
        print('sa',x,xi,self.min,self.max,self.N)
        self.a[xi] += 1
        self.sqa[xi//self.sq] += 1

    def pop(self, x):
        cnt = 0
        for i in range(self.sq+1):
            if cnt + self.sqa[i] >= x:
                self.sqa[i] -= 1
                break
            cnt += self.sqa[i]
        ai = self.sq * i
        print('sp',x,self.min,self.max,self.N, cnt,i)
        for i in range(self.sq):
            print('spi', ai+i)
            cnt += self.a[ai+i]
            if cnt >= x:
                self.a[ai+i] -= 1
                return ai+i


class DecompositionTree():

    def __init__(self, mi, ma, k):
        self.min = mi
        self.max = ma
        n = ma - mi
        self.N = n
        s = int(math.pow(n, 1.0 / k))
        cs = n // s
        self.cs = cs
        self.size = s
        if k == 3:
            self.a = [SquareDecomposition(mi+cs*c, mi+cs*(s+1)-1) for c in range(s+1)]
        else:
            self.a = [DecompositionTree(mi+cs*c, mi+cs*(c+1)-1, k-1) for c in range(s+1)]
        self.cnt = 0
        self.ca = [0] * (s+1)

    def add(self, x):
        xi = (x - self.min) // self.cs
        print('Da',x,xi,self.min,self.max,self.size,self.cs)
        self.cnt += 1
        self.ca[xi] += 1
        self.a[xi].add(x)

    def pop(self, x):
        print('Dp',x,self.min,self.max,self.size,self.cs,self.cnt)
        cnt = 0
        for i in range(self.size+1):
            if cnt + self.ca[i] >= x:
                self.ca[i] -= 1
                self.cnt -= 1
                return self.a[i].pop(x)
                break
            cnt += self.ca[i]


def main():
    n = int(input())
    sd = DecompositionTree(1, 200001, 3)
    for _ in range(n):
        q, x = list(map(int, input().split()))
        if q == 1:
            sd.add(x)
            continue
        print(sd.pop(x))


main()
