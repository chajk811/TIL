import sys
sys.stdin = open('2105_input.txt')

dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]

def find(x, y, idx, order):
    global MAX
    if idx > 3:
        return
    nx = x + dx[idx]
    ny = y + dy[idx]

    if 0 <= nx < N and 0 <= ny < N:
        if (nx, ny) == (i, j): # 한바퀴 돌고 출발점으로 돌아왔으면
            if len(order) > MAX:
                MAX = len(order) # 최대값 갱신
                return
        if arr[nx][ny] in order: # 같은 숫자가 있으면 끝냄
            return
        order.append(arr[nx][ny])
        find(nx, ny, idx, order) # 현재 방향으로 계속 방문
        find(nx, ny, idx+1, order) # 다음 방향으로 방문
        order.pop()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    MAX = -1

    for i in range(0, N-1):
        for j in range(0, N-1):
            find(i, j, 0, [arr[i][j]])

    print('#{} {}'.format(tc, MAX))

