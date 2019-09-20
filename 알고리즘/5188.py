import sys
sys.stdin = open('5188_input.txt')

# 우, 하
dx = [0, 1]
dy = [1, 0]

def BFS():
    Q.append((0, 0))
    visited[0][0] = arr[0][0]

    while Q:
        x, y = Q.pop(0)

        if x == N-1 and y == N-1:
            return visited[x][y]

        for d in range(2):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    Q = []
    visited = [[0]*N for _ in range(N)]

    print('#{} {}'.format(tc, BFS()))