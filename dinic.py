# http://topcoder.g.hatena.ne.jp/Mi_Sawa/20140311
#   https://gist.github.com/MiSawa/9532038 を写経した
class E:
    def __init__(self, dst, cap, rev):
        self.dst = dst
        self.cap = cap
        self.rev = rev

    def __repr__(self):
        return "({}, {}, {})".format(self.dst, self.cap, self.rev)

    def __str__(self):
        return "({}, {}, {})".format(self.dst, self.cap, self.rev)

class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, src, dst, cap):
        self.g[src].append(E(dst, cap, len(self.g[dst])))
        self.g[dst].append(E(src, 0, len(self.g[src]) - 1))

    def add_undirected_edge(self, src, dst, cap):
        self.g[src].append(E(dst, cap, len(self.g[dst])))
        self.g[dst].append(E(src, cap, len(self.g[src]) - 1))

    def dfs(self, s, u, crr):
        if s == u or crr == 0:
            return crr
        sm = 0
        for i in range(self.itr[u], len(self.g[u])):
            e = self.g[u][i]
            ee = self.g[e.dst][e.rev]
            v = e.dst
            if self.level[v] >= self.level[u] or ee.cap <= 0:
                continue
            f = self.dfs(s, v, min(crr - sm, ee.cap))
            if f <= 0:
                continue
            ee.cap -= f
            e.cap += f
            sm += f
            if sm == crr:
                break
        return sm
