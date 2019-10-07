dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def check(tmp, d):
    if d == 1:
        now = tmp[::]
        tmp[2] = now[6]
        tmp[3] = now[2]
        tmp[4] = now[3]
        tmp[6] = now[4]
        return

    elif d == 2:
        now = tmp[::]
        tmp[2] = now[3]
        tmp[3] = now[4]
        tmp[4] = now[6]
        tmp[6] = now[2]
        return

    elif d == 3:
        now = tmp[::]
        tmp[1] = now[3]
        tmp[3] = now[5]
        tmp[5] = now[6]
        tmp[6] = now[1]
        return

    elif d == 4:
        now = tmp[::]
        tmp[1] = now[6]
        tmp[3] = now[1]
        tmp[5] = now[3]
        tmp[6] = now[5]
        return


N, M, x, y, K = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
tmp = [0] * 7

for i in range(K):
    tmp_x, tmp_y = x, y
    d = order[i]
    x = x + dx[d]
    y = y + dy[d]
    if 0 <= x < N and 0 <= y < M:
        check(tmp, d)
        if not m[x][y]:
            m[x][y] = tmp[6]
        else:
            tmp[6] = m[x][y]
            m[x][y] = 0
    else:
        x, y = tmp_x, tmp_y
        continue
    print(tmp[3])