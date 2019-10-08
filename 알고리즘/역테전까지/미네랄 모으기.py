import sys
sys.stdin = open('미네랄모으기_input.txt')

def find(s, e, battery, tmp):
    global MAX

    if battery <= 1:
        MAX = max(tmp, MAX)
        return
    if s == e:
        MAX = max(tmp, MAX)
        return

    move = abs(robot[0] - minerals[s][0]) + abs(robot[1] - minerals[s][1])
    get = arr[minerals[s][0]][minerals[s][1]]

    if move * 2 > battery:
        find(s+1, e, battery, tmp)
    else:
        find(s+1, e, battery - (move * 2), tmp + get)
        find(s+1, e, battery, tmp)

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minerals = []
    robot = []
    MAX = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                robot = [i, j]
            elif arr[i][j]:
                minerals.append([i, j])

    find(0, len(minerals), C, 0)
    print('#{} {}'.format(tc, MAX))