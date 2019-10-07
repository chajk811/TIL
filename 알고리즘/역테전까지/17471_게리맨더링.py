import copy

def subset():
    global MIN

    cnt = 0
    for i in range(1, (1 << N)//2):
        subset_tmp = []
        for j in range(N):
            if i & (1 << j):
                subset_tmp.append(subset_list[j])

        g1 = subset_tmp
        g2 = list(set(subset_list) - set(subset_tmp))

        a, b = check(g1, g2)

        if a == 1 and b == 1:
            cnt1, cnt2 = 0, 0
            for v in range(1, N+1):
                if v in g1:
                    cnt1 += P[v]
                if v in g2:
                    cnt2 += P[v]
            if MIN > abs(cnt1 - cnt2):
                MIN = abs(cnt1 - cnt2)


def check(g1, g2):
    arr_g1 = copy.deepcopy(arr)
    arr_g2 = copy.deepcopy(arr)

    for i in range(1, N+1):
        if i in g2:
            arr_g1[i] = [0] * (N+1)
        if i in g1:
            arr_g2[i] = [0] * (N+1)
        for j in range(1, N+1):
            if j in g2:
                arr_g1[i][j] = 0
            if j in g1:
                arr_g2[i][j] = 0


    if len(g1) == 1:
        return 1, BFS(arr_g2, g2)
    elif len(g2) == 1:
        return BFS(arr_g1, g1), 1
    else:
        return BFS(arr_g1, g1), BFS(arr_g2, g2)


def BFS(arre, g):
    visited = [0] * (N+1)
    Q = [g[0]]

    while Q:
        t = Q.pop(0)
        visited[t] = 1

        for i in range(1, N+1):
            if arre[t][i] == 1 and visited[i] == 0:
                Q.append(i)

    for i in range(1, N+1):
        if i in g:
            if visited[i] == 0:
                return 0
    return 1

N = int(input())
P = [0] + list(map(int, input().split()))
arr = [[0] * (N+1) for _ in range(N+1)]
MIN = 0xfffffff

for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0]+1):
        arr[i][tmp[j]] = 1

subset_list = [i for i in range(1, N+1)]
subset()
if MIN != 0xfffffff:
    print(MIN)
else:
    print(-1)