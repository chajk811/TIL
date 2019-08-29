import sys
sys.stdin = open('5105_input.txt')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    global cnt
    Q.append([x, y])
    visited[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if nx == gx and ny == gy:
                    visited[nx][ny] += visited[x][y] + 1
                    cnt = visited[nx][ny]
                    return
                if arr[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] += visited[x][y] + 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[0]*N for i in range(N)]

    Q = []
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                gx, gy = i, j
            if arr[i][j] == 2:
                x, y = i, j

    BFS(x, y)

    if not cnt:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, cnt-2))

    for _ in range(N):
        print(visited[_])




