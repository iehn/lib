
def _kosa(a1, a2, b1, b2):
    x1,y1 = a1
    x2,y2 = a2
    x3,y3 = b1
    x4,y4 = b2

    tc = (x1-x2)*(y3-y1)+(y1-y2)*(x1-x3)
    td = (x1-x2)*(y4-y1)+(y1-y2)*(x1-x4)
    return tc*td < 0

def kosa(a1, a2, b1, b2):
    return _kosa(a1,a2,b1,b2) and _kosa(b1,b2,a1,a2)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def distance_p(a, b):
    return distance(a[0], a[1], b[0], b[1])

def radian(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)

# (distance, radian)
def drx(d, r):
    return math.cos(r) * d

def dry(d, r):
    return math.sin(r) * d

# 交点
def intersection(a1, a2, b1, b2):
    x1,y1 = a1
    x2,y2 = a2
    x3,y3 = b1
    x4,y4 = b2

    ksi = (y4 - y3) * (x4 - x1) - (x4 - x3) * (y4 - y1)
    eta = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
    delta = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if delta == 0:
        return None
    ramda = ksi / delta;
    mu = eta / delta;
    if ramda >= 0 and ramda <= 1 and mu >= 0 and mu <= 1:
        return (x1 + ramda * (x2 - x1), y1 + ramda * (y2 - y1))

    return None

# 円の交点, pはx,y,r
def polar(a, r):
    return (math.cos(r) * a, math.sin(r) * a)

def intersection_c(ap, bp):
    ax,ay,ar = ap
    bx,by,br = bp
    d = distance(ax,ay,bx,by)
    if d > ar + br or d < abs(ar - br):
        return None

    ac = math.acos((ar**2 + d**2 - br**2) / (2 * ar * d))
    t = math.atan2(by - ay, bx - ax)
    r1 = polar(ar, t + ac)
    r2 = polar(ar, t - ac)
    return [(ax+r1[0], ay+r1[1]), (ax+r2[0], ay+r2[1])]


# 線分p1-p2と点p3の距離, p1,p2,p3は[x,y]の配列
def distance3(p1, p2, p3):
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3

    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    r = (ax*bx + ay*by) / (ax*ax + ay*ay)
    if r <= 0:
        return distance_p(p1, p3)
    if r >= 1:
        return distance_p(p2, p3)
    pt = (x1 + r*ax, y1 + r*ay, 0)
    return distance_p(pt, p3)

### 三角形, xy は要素3,2の配列

# 面積
def area(xy):
    xy = sorted(xy)
    x = [xy[i][0] - xy[0][0] for i in range(3)]
    y = [xy[i][1] - xy[0][1] for i in range(3)]
    return abs(x[1]*y[2] - x[2]*y[1]) / 2

# 三辺版
def area(a, b, c):
    s = (a+b+c) / 2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

# 内接円の半径
def inside_r(xy):
    s = area(xy)
    a = [((xy[i][0] - xy[i-1][0])**2 + (xy[i][1] - xy[i-1][1])**2) ** 0.5 for i in range(3)]
    return 2 * s / sum(a)

# 外心
# 直線上にある場合はエラーになるので、distance3のr判定をなくしたものでの判定を先に入れる
def gaisin(xy):
    a = xy[0][0]
    b = xy[0][1]
    c = xy[1][0]
    d = xy[1][1]
    e = xy[2][0]
    f = xy[2][1]

    t1 = (e-a) * (a**2 + b**2 - c**2 - d**2)
    t2 = (c-a) * (a**2 + b**2 - e**2 - f**2)
    t3 = 2 * (e-a) * (b-d) - 2 * (c-a) * (b-f)
    py = (t1 - t2) / t3
    if c - a == 0:
        px = (2 * (b-d) * py - a**2 - b**2 + c**2 + d**2) / (2 * (c-a))
    else:
        px = (2 * (b-f) * py - a**2 - b**2 + e**2 + f**2) / (2 * (e-a))
    return (px, py)

### 凸包, 引数は2要素(xy)の配列もしくはその配列
def ccw(a, b, c):
    ax = b[0] - a[0]
    ay = b[1] - a[1]
    bx = c[0] - a[0]
    by = c[1] - a[1]
    t = ax*by - ay*bx;
    if t > 0:
        return 1
    if t < 0:
        return -1
    if ax*bx + ay*by < 0:
        return 2
    if ax*ax + ay*ay < bx*bx + by*by:
        return -2
    return 0

def convex_hull(ps):
    n = len(ps)
    k = 0
    ps.sort()
    ch = [None] * (n*2)
    for i in range(n):
        while k >= 2 and ccw(ch[k-2], ch[k-1], ps[i]) <= 0:
            k -= 1
        ch[k] = ps[i]
        k += 1
    t = k + 1
    for i in range(n-2,-1,-1):
        while k >= t and ccw(ch[k-2], ch[k-1], ps[i]) <= 0:
            k -= 1
        ch[k] = ps[i]
        k += 1

    return ch[:k-1]

def radian(a, b):
    return math.atan2(b[1]-a[1], b[0]-a[0])
