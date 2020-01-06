class AVLTree:
    LEFT = 0
    RIGHT = 1

    class Node:
        def __init__(self, x):
            self.data  = x
            self.l  = None
            self.r = None
            self.h = 1

    def __init__(self):
        self.root = None

    def get_h(self, n):
        if n.l:
            a = n.l.h
        else:
            a = 0
        if n.r:
            b = n.r.h
        else:
            b = 0
        return max(a, b) + 1

    def get_balance(self, n):
        if n.l:
            a = n.l.h
        else:
            a = 0
        if n.r:
            b = n.r.h
        else:
            b = 0
        return a - b

    def rotate_r(self, n):
        ln = n.l
        n.l = ln.r
        ln.r = n
        n.h = get_h(n)
        ln.h = get_h(ln)
        return ln

    def rotate_l(self, n):
        rn = n.r
        n.r = rn.l
        rn.l = n
        n.h = get_h(n)
        rn.h = get_h(rn)
        return rn

    def search(self, n, x):
        while n:
            if n.data == x: return True
            if x < n.data:
                n = n.l
            else:
                n = n.r
        return False

    def balance(self, path):
        while len(path) > 0:
            new_n = None
            n, dir = path.pop()
            h = get_h(n)
            if h == n.h: return self.root   # 高さに変化なし
            b = get_balance(n)
            if b > 1:
                if get_balance(n.l) < 0:
                    # ２重回転
                    n.l = rotate_l(n.l)
                new_n = rotate_r(n)
            elif b < -1:
                if get_balance(n.r) > 0:
                    # ２重回転
                    n.r = rotate_r(n.r)
                new_n = rotate_l(n)
            else:
                n.h = h
            if new_n:
                # 子の付け替え
                if len(path) > 0:
                    # n の親節を求める
                    pn, pdir = path[len(path) - 1]
                    if pdir == LEFT:
                        pn.l = new_n
                    else:
                        pn.r = new_n
                else:
                    return new_n
        return self.root

    # 挿入
    def insert(self, self.root, x):
        if self.root is None: return Node(x)
        path = []
        p = self.root
        while True:
            if p.data == x: return self.root
            elif x < p.data:
                path.append((p, LEFT))
                if not p.l:
                    p.l = Node(x)
                    break
                p = p.l
            else:
                path.append((p, RIGHT))
                if not p.r:
                    p.r = Node(x)
                    break
                p = p.r
        return balance(path)

    # データを探す
    def _search(self, n, x, path):
        while n:
            if n.data == x: return n
            if x < n.data:
                path.append((n, LEFT))
                n = n.l
            else:
                path.append((n, RIGHT))
                n = n.r
        return None

    # 最小値を探す
    def _search_min(self, n, path):
        while n.l:
            path.append((n, LEFT))
            n = n.l
        return n

    # 削除
    def delete(self, self.root, x):
        if self.root is None: return None    # 空の木
        path = []                       # 経路
        n = _search(self.root, x, path)   # 探索
        if n is None: return self.root    # 削除データなし
        if n.l and n.r:
            # 子が二つある場合
            # 右部分木の最小値を探して置き換える
            path.append((n, RIGHT))
            min_n = _search_min(n.r, path)
            n.data = min_n.data
            n = min_n
        if len(path) > 0:
            pn, dir = path[len(path) - 1]
        else:
            pn = None
        # 節を削除する
        if n.l is None:
            cn = n.r
        else:
            cn = n.l
        if pn is None:
            return cn        # self.root の削除
        elif dir == LEFT:
            pn.l = cn
        else:
            pn.r = cn
        return balance(path)

    # 巡回
    def traverse(self, n):
        if n:
            for x in traverse(n.l):
                yield x
            yield n.data
            for x in traverse(n.r):
                yield x
