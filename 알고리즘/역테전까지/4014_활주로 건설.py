import sys
sys.stdin = open('4014_input.txt')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find():
    global C

    for i in range(N):
        built = [0] * N
        for j in range(N):
            # 현재 위치 arr[i][j], 열 검사
            check = check1(i, j, built)
            if not check:
                break
        else:
            C += 1

    for m in range(N):
        built = [0] * N
        for n in range(N):
            # 현재 위치 arr[n][m], 행 검사
            check = check2(n, m, built)
            if not check:
                break
        else:
            C += 1


def check1(x, y, built):
    for d in range(2, 4):
        ny = y + dy[d]
        build = 0
        if 0 <= ny < N:
            if arr[x][y] > arr[x][ny]:
                if abs(arr[x][y] - arr[x][ny]) == 1:
                    cnt = X - 1
                    tmp = arr[x][ny]
                    while cnt:
                        ny = ny + dy[d]
                        if not(0 <= ny < N) or arr[x][ny] != tmp:
                            return 0
                        if built[ny] == 1:
                            return 0
                        cnt -= 1
                    build = 1
                else:
                    return 0
    if build == 1:
        for b in range(y+1, y+1+X):
            built[b] = 1
    return 1

def check2(x, y, built):
    for d in range(2):
        nx = x + dx[d]
        build = 0
        if 0 <= nx < N:
            if arr[x][y] > arr[nx][y]:
                if abs(arr[x][y] - arr[nx][y]) == 1:
                    cnt = X - 1
                    tmp = arr[nx][y]
                    while cnt:
                        nx = nx + dx[d]
                        if not(0 <= nx < N) or arr[nx][y] != tmp:
                            return 0
                        if built[nx] == 1:
                            return 0
                        cnt -= 1
                    build = 1
                else:
                    return 0
    if build == 1:
        for b in range(x+1, x+1+X):
            built[b] = 1
    return 1

T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    C = 0
    find()
    print('#{} {}'.format(tc, C))