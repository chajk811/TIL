import sys
sys.stdin = open('원자소멸시뮬레이션_input.txt')

# 상 하 좌 우 0 1 2 3
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move():
    global E

    # 1초 이동 후 원자들의 위치
    for i in point:
        for d in range(4):
            if i[2] == d:
                nx = dx[d] + i[0]
                ny = dy[d] + i[1]
                if -1000 > nx or nx > 1000 or -1000 > ny or ny > 1000:
                    point.remove(i)
                else:
                    i[0] = nx
                    i[1] = ny

    # 같은것 삭제
    picked = [0] * len(point)

    for p in range(len(point)):
        pick = point[p]
        for c in range(len(point)):
            if pick == point[c]:
                continue
            elif point[c][0] == pick[0] and point[c][1] == pick[1] and picked[c] == 0:
                S.append(point[c])
                picked[c] = 1
        else:
            if len(S) > 0 and S[-1][0] == pick[0] and S[-1][1] == pick[1] and picked == 0:
                S.append(pick)

    while S:
        n = S.pop()
        for pp in point:
            if n == pp:
                E += pp[3]
                point.remove(n)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    point = [list(map(int, input().split())) for _ in range(N)]

    E = 0
    S = []
    n = 0

    while n < 10:
        move()
        n += 1