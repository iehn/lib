# 下がtrue, falseになる最小値を返す
def bs(f, mi, ma):
    mm = -1
    while ma > mi:
        mm = (ma+mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

# 再帰版
def bs(f, mi, ma):
    mm = (ma+mi) // 2

    if ma <= mi:
        if f(mm):
            return mm + 1
        return mm

    if f(mm):
        mi = mm + 1
    else:
        ma = mm

    return bs(f, mi, ma)

# 小数版 epsで制度調整する
def bs(f, mi, ma):
    mm = -1
    while ma > mi + eps:
        mm = (ma+mi) / 2.0
        if f(mm):
            mi = mm + eps
        else:
            ma = mm
    if f(mm):
        return mm + eps
    return mm

# 分数版 少数版では誤差で死ぬ場合に使う, timeoutも設定する
def bs(f, mi, ma):
    st = time.time()
    mm = -1
    mi = fractions.Fraction(mi, 1)
    ma = fractions.Fraction(ma, 1)
    while ma > mi + eps:
        gt = time.time()
        mm = (ma+mi) / 2
        if gt - st > 35:
            return mm
        if isinstance(mm, float):
            tk = max(1, int(10**15 / mm))
            mm = fractions.Fraction(int(mm*tk), tk)
        if float(mm) == float(ma) or float(mm) == float(mi):
            return mm
        if f(mm):
            mi = mm
        else:
            ma = mm
    if f(mm):
        return mm + eps
    return mm
