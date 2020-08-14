class BellmanFord:
    def __init__(self, n):
        self.N = n
        self.e = collections.defaultdict(list)

    def add(self, u, v, d):
        self.e[u].append((v,d))

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]

    def search(self, s):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        update = True
        cnt = 0
        while update:
            cnt += 1
            if cnt > self.N:
                return d,True
            update = False
            for k,v in self.e.items():
                if d[k] == inf:
                    continue
                dk = d[k]
                for n,nd in v:
                    if d[n] > dk + nd:
                        update = True
                        d[n] = dk + nd

        return d,False

    # メソッドのみ版
    def search(s, N):
        d = collections.defaultdict(lambda: inf)
        d[s] = 0
        update = True
        cnt = 0
        while update:
            cnt += 1
            if cnt > N:
                return d,True
            update = False
            for k,v in e.items():
                if d[k] == inf:
                    continue
                dk = d[k]
                for n,nd in v:
                    if d[n] > dk + nd:
                        update = True
                        d[n] = dk + nd

        return d,False

