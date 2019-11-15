import sys
sys.stdin = open('1949_input.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def DFS(x, y, cut, cnt):
    global MAX
    if cnt > MAX:
        MAX = cnt

    for m in range(4):
        nx = x + dx[m]
        ny = y + dy[m]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if M[nx][ny] < M[x][y]:
                visited[nx][ny] = 1
                DFS(nx, ny, cut, cnt+1)
                visited[nx][ny] = 0

            elif not cut:
                for k in range(1, K+1):
                    if M[nx][ny] - k < M[x][y]:
                        M[nx][ny] -= k
                        visited[nx][ny] = 1

                        DFS(nx, ny, True, cnt+1)

                        visited[nx][ny] = 0
                        M[nx][ny] += k
                        break


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]

    hight = 0

    for i in range(N):
        if hight < max(M[i]):
            hight = max(M[i])

    MAX = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if M[i][j] == hight:
                visited[i][j] = 1
                DFS(i, j, False, 1)
                visited[i][j] = 0

    print('#{} {}'.format(tc, MAX))





