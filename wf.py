class WarshallFloyd():
    def __init__(self, e, n):
        self.E = e
        self.N = n

    def search(self):
        n = self.N
        nl = list(range(n))
        d = [[inf] * n for _ in nl]
        for i in range(n):
            d[i][i] = 0
        for k,v in self.E.items():
            dk = d[k]
            for b,c in v:
                # consider multiple edges
                if dk[b] > c:
                    dk[b] = c
        for i in nl:
            di = d[i]
            for j in nl:
                if i == j:
                    continue
                dj = d[j]
                for k in nl:
                    if i != k and j != k and dj[k] > dj[i] + di[k]:
                        dj[k] = dj[i] + di[k]
        return d
