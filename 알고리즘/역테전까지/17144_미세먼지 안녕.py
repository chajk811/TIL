import sys
sys.stdin = open('17144_input.txt')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move():
    global arr, air
    tmp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                tmp[i][j] = -1
                if len(air) != 2:
                    air.append(i)
            elif arr[i][j] > 0:
                x, y = i, j
                now = arr[i][j]
                cnt = 0
                for d in range(4):
                    nx = dx[d] + x
                    ny = dy[d] + y
                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                        tmp[nx][ny] += now // 5
                        cnt += 1
                tmp[x][y] += now - (now//5) * cnt
    arr = tmp

def delete():
    global arr

    x, y = air[0], 1
    wind = []

    while y < C-1:
        wind.append(arr[x][y])
        y += 1
    while x > 0:
        wind.append(arr[x][y])
        x -= 1
    while y > 0:
        wind.append(arr[x][y])
        y -= 1
    while x < air[0]:
        wind.append(arr[x][y])
        x += 1

    wind = [0] + wind[:len(wind)-1]
    x, y = air[0], 1
    cnt = 0

    while y < C-1:
        arr[x][y] = wind[cnt]
        cnt += 1
        y += 1
    while x > 0:
        arr[x][y] = wind[cnt]
        cnt += 1
        x -= 1
    while y > 0:
        arr[x][y] = wind[cnt]
        cnt += 1
        y -= 1
    while x < air[0]:
        arr[x][y] = wind[cnt]
        cnt += 1
        x += 1
    #-----------------
    x, y = air[1], 1
    wind = []

    while y < C-1:
        wind.append(arr[x][y])
        y += 1
    while x < R-1:
        wind.append(arr[x][y])
        x += 1
    while y > 0:
        wind.append(arr[x][y])
        y -= 1
    while x > air[1]:
        wind.append(arr[x][y])
        x -= 1

    wind = [0] + wind[:len(wind)-1]
    x, y = air[1], 1
    cnt = 0

    while y < C-1:
        arr[x][y] = wind[cnt]
        cnt += 1
        y += 1
    while x < R-1:
        arr[x][y] = wind[cnt]
        cnt += 1
        x += 1
    while y > 0:
        arr[x][y] = wind[cnt]
        cnt += 1
        y -= 1
    while x > air[1]:
        arr[x][y] = wind[cnt]
        cnt += 1
        x -= 1


T = int(input())

for tc in range(1, T+1):
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    air = []
    result = 0


    for t in range(T):
        move()
        delete()

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                result += arr[i][j]

    print(result)