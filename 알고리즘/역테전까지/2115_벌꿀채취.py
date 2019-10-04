import sys
sys.stdin = open('2115_input.txt')

def check():
    global MAX
    tmp = 0

    for p in range(2):
        if sum(person[p]) <= C:
            for s in person[p]:
                tmp += s * s
        else:
            subset_MAX = 0
            for m in range(1, 1 << M):
                subset_tmp = []
                for n in range(M):
                    if m & (1 << n):
                        subset_tmp.append(person[p][n])
                if sum(subset_tmp) <= C:
                    result = 0
                    for st in subset_tmp:
                        result += st * st
                    if subset_MAX < result:
                        subset_MAX = result
            tmp += subset_MAX

    if tmp > MAX:
        MAX = tmp


def comb(cnt, sr, sc):
    if cnt == 2:
        check()
        return

    j = sc
    for i in range(sr, N):
        while j <= (N-M):
            if not visited[i][j]:
                person[cnt] = [arr[i][k] for k in range(j, j+M)]
                for k in range(j, j+M):
                    visited[i][k] = 1
                comb(cnt+1, i, j+M)
                for k in range(j, j+M):
                    visited[i][k] = 0
            j += 1
        j = 0


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    person = [0] * 2
    MAX = 0

    comb(0, 0, 0)
    print('#{} {}'.format(tc, MAX))

