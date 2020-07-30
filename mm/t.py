import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools,os

eps = 1.0 / 1e9
cs = collections.defaultdict(list)
ks = collections.defaultdict(list)
kt = [1] * 100

for i in range(100, 400):
    name = 'k/{}.txt'.format(i)
    if not os.path.exists(name):
        break
    li = i
    with open(name, 'r') as f:
        d = list(map(lambda x: x.split(), f.read().split('\n')[:-1]))
        ts = [_ for _ in d if len(_) > 2 and _[0] == 'Score']

        if len(ts) < 10:
            continue
        for i in range(len(ts)):
            t = float(ts[i][2])
            if t < 0:
                continue
            cs[i].append(t)


cil = [100]
for i in list(range(100, 400)) + [cil[-1]]:
    if i not in cil and i < cil[-1]:
        continue
    name = 'k/{}.txt'.format(i)
    ti = i
    if not os.path.exists(name):
        continue
    print("")
    with open(name, 'r') as f:
        mt = 0
        d = list(map(lambda x: x.split(), f.read().split('\n')[:-1]))
        t = [float(_[2]) for _ in d if len(_) > 2 and _[0] == 'Score']
        if len(t) < 10:
            continue
        scores = []
        ec = 0
        for i in range(len(t)):
            if t[i] < 1e-9:
                ec += 1
                if ti == li:
                    print("error ", i)
                scores.append((0, i))
            else:
                scores.append((min(cs[i]) / t[i], i))
        ss = sorted(scores)
        sc = list(map(lambda x: x[0], scores))
        avg = sum(sc) / len(sc)
        ml = len([c for c in sc if c == 1.0])
        print("{} avg: {}, low: {}, len: {}, nea: {} ml: {} ec: {}".format(name, avg, sum(t) / len(sc), len(sc), sum(sc) / (len(sc) - ec), ml, ec))

        epc = 1 if ti < li-1 and ti != cil[-1] else 5
        pc = 0
        i = 0
        while pc < epc:
            m = ss[i][0]
            mi = ss[i][1]
            i += 1
            if min(cs[mi]) < 0:
                continue
            print("min{}: {}, seed: {}, t: {}, mint: {}, mini: {}".format(i, m, mi+100000, t[mi], min(cs[mi]), len(cs[mi]) - cs[mi][::-1].index(min(cs[mi])) + 99))
            pc += 1

