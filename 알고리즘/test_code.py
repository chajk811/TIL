import sys
sys.stdin = open('원자소멸시뮬레이션_input.txt')

T = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

crush = {0: 1, 1: 0, 2: 3, 3: 2}


def BFS(q):
    global count
    new = {}
    new_q = []
    de = []
    while len(q) > 0:
        x, y, d, k = q.pop(0)

        if (x, y) in de:
            continue

        nx = x + dx[d]
        ny = y + dy[d]

        if rx <= nx <= hx and ry <= ny <= hy:
            # 스쳐 부딪일때
            if (nx, ny) in M_dict.keys() and crush[d] == M_dict[(nx, ny)][0]:
                # if M[nx][ny] and crush[d] == M[nx][ny][0]:
                count += (k + M_dict[(nx, ny)][1])
                del M_dict[(nx, ny)]
                # M[nx][ny] = 0
                de.append((nx, ny))

            else:
                # 동시에 같은 자리에 경우도 없으면
                if (nx, ny) not in new.keys():
                    new[(nx, ny)] = [d, k]

                # 동시에 같은 자리에 가는 경우가 있으면
                else:
                    new[(nx, ny)].append(k)

        # M[x][y] = 0
        del M_dict[(x, y)]

    for k, v in new.items():
        x, y = k

        if len(v) > 2:
            count += sum(v[1:])
        else:
            new_q.append((x, y, v[0], v[1]))
            M_dict[(x, y)] = (v[0], v[1])
            # M[x][y] = (v[0],v[1])

    return new_q


for tc in range(T):
    N = int(input())
    # M = [[0]*2001 for _ in range(2001)]
    M_dict = {}
    Q = []

    count = 0
    rx = 0xfffffff
    hx = 0
    ry = 0xfffffff
    hy = 0

    for _ in range(N):
        # 가로 높이
        i, j, d, k = map(int, input().split())

        x = -(j) + 1000

        y = i + 1000

        if x < rx:
            rx = x
        if x > hx:
            hx = x
        if y < ry:
            ry = y
        if y > hy:
            hy = y

        Q.append((x, y, d, k))
        M_dict[(x, y)] = (d, k)
        # M[x][y] = (d,k)

    while len(Q) > 0:
        Q = BFS(Q)

    print("#{} {}".format(tc + 1, count))