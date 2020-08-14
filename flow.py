# 汎用版, edgeはN*Nの2次元配列, capで速くなった
class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N

    def max_flow(self, s, t):
        r = 0
        e = self.E

        def f(c, cap):
            v = self.v
            v[c] = 1
            if c == t:
                return cap
            for i in range(self.N):
                if v[i] or e[c][i] <= 0:
                    continue
                cp = min(cap, e[c][i])
                k = f(i, cp)
                if k > 0:
                    e[c][i] -= k
                    e[i][c] += k
                    return k
            return 0

        while True:
            self.v = [None] * self.N
            fs = f(s, inf)
            if fs == 0:
                break
            r += fs

        return r

# 速度調整版, edgeはset, 重さは1固定
class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N
        self.nl = list(range(N))

    def max_flow(self, s, t):
        r = 0
        e = self.E
        v = None

        def f(c):
            v[c] = 1
            if c == t:
                return 1
            for i in e[c]:
                if v[i] is None and f(i):
                    e[c].remove(i)
                    e[i].add(c)
                    return 1
            return

        while True:
            v = [None] * self.N
            if f(s) is None:
                break
            r += 1

        return r


# 重み付き2部マッチング(最小コストのを追加していく, 問題によると思うけど、速度が速いっぽい)
class Edge():
    def __init__(self,t,f,r,ca,co):
        self.to = t
        self.fron = f
        self.rev = r
        self.cap = ca
        self.cost = co

class MinCostFlow():
    size = 0
    graph = []

    def __init__(self, s):
        self.size = s
        self.graph = [[] for _ in range(s)]

    def add_edge(self, f, t, ca, co):
        self.graph[f].append(Edge(t, f, len(self.graph[t]), ca, co))
        self.graph[t].append(Edge(f, t, len(self.graph[f])-1, 0, -co))

    def min_path(self, s, t):
        dist = [inf] * self.size
        route = [None] * self.size
        que = collections.deque()
        inq = [False] * self.size
        dist[s] = 0
        que.append(s)
        inq[s] = True
        while que:
            u = que.popleft()
            inq[u] = False
            for e in self.graph[u]:
                if e.cap == 0:
                    continue
                v = e.to
                if dist[v] > dist[u] + e.cost:
                    dist[v] = dist[u] + e.cost
                    route[v] = e
                    if not inq[v]:
                        que.append(v)
                        inq[v] = True

        if dist[t] == inf:
            return inf, 0

        flow = inf
        v = t
        while v != s:
            e = route[v]
            if flow > e.cap:
                flow = e.cap
            v = e.fron

        c = 0
        v = t
        while v != s:
            e = route[v]
            e.cap -= flow
            self.graph[e.to][e.rev].cap += flow
            c += e.cost * flow
            v = e.fron

        return dist[t], flow

    def calc_min_cost_flow(self, s, t, flow):
        total_cost = 0
        while flow > 0:
            c,f = self.min_path(s, t)
            if f == 0:
                return inf
            f = min(flow, f)
            total_cost += c * f
            flow -= f

        return total_cost


# 使用例( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2293 )
def main():
    n = I()
    mcf = MinCostFlow(4096)
    s = 4094
    t = 4095
    for i in range(n):
        mcf.add_edge(s, i, 1, 0)
        mcf.add_edge(i, 4093, 1, 0)

    a = []
    b = []
    ss = set()
    for _ in range(n):
        ai,bi = LI()
        a.append(ai)
        b.append(bi)
        ss.add(ai)
        ss.add(bi)
    d = {}
    for i,v in zip(range(len(ss)), sorted(ss)):
        d[v] = i + n
        mcf.add_edge(i+n, t, 1, 0)
    mcf.add_edge(4093, t, inf, 0)
    for i in range(n):
        mcf.add_edge(i, d[a[i]], 1, -b[i])
        mcf.add_edge(i, d[b[i]], 1, -a[i])
    res = mcf.calc_min_cost_flow(s, t, n)
    return -res
