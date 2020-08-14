# 強連結成分分解
# n=size, e,reはsetで有向辺と逆
# 強連結成分のidの配列を返す(わかりづらいがUnionFindと同じ感じで扱いたかった)
def scc(n, e, re):
    v = [None] * n
    t = []
    def dfs(i):
        v[i] = 0
        for b in e[i]:
            if v[b] is None:
                dfs(b)
        t.append(i)

    for i in range(n):
        if v[i] is None:
            dfs(i)

    r = [None] * n
    def dfs2(i, p):
        r[i] = p
        for b in re[i]:
            if r[b] is None:
                dfs2(b, p)

    for c in t[::-1]:
        if r[c] is None:
            dfs2(c, c)

    return r
