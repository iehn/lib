
# 雑な実装, 大きな問題で速度調整したい
# 深さをもたせてみてるが、使ったことはない
class Trie():
    def __init__(self, n):
        self.n = n
        self.c = 0
        self.cl = collections.defaultdict(lambda: Trie(self.n+1))

    def add(self, a):
        self.c += 1
        if len(a) == 0:
            return
        self.cl[a[0]].add(a[1:])

    def __str__(self):
        s = '{}:'.format(self.c)
        for k,v in self.cl.items():
            s += ' ({}: {})'.format(k, v.c)
        return s
