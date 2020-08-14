# 蟻本 4-1
# Ax=bを解く, Aは正方行列, 解がないor一意でない場合はNoneを返す
def gauss_jordan(A, b):
    n = len(A)
    B = [A[i][:] for i in range(n)]
    for i in range(n):
        B[i].append(b[i])

    for i in range(n):
        pivot = i
        abp = abs(B[i][i])
        for j in range(i+1, n):
            if abp < abs(B[j][i]):
                abp = abs(B[j][i])
                pivot = j
        B[i],B[pivot] = B[pivot],B[i]
        if abp < eps:
            return

        for j in range(i+1, n+1):
            B[i][j] /= B[i][i]
        for j in range(n):
            if j == i:
                continue
            for k in range(i+1, n+1):
                B[j][k] -= B[j][i] * B[i][k]

    return list(map(lambda x: x[-1], B))
