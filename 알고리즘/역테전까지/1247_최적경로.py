import sys
sys.stdin = open('1247_input.txt')

# DFS
# def find(cnt, start, tmp):
#     global MIN
#
#     if MIN <= tmp + arr[start][1]:
#         return
#     if cnt == N:
#         if MIN > tmp + arr[start][1]:
#             MIN = tmp + arr[start][1]
#             return
#
#     pick[start] = 1
#     for i in range(2, N+2):
#         if pick[i]:
#             continue
#         find(cnt+1, i, tmp + arr[start][i])
#     pick[start] = 0

def find(cnt, start, tmp):
    global MIN

    if MIN <= tmp + arr[start][1]:
        return

    if cnt == N:
        if MIN > tmp + arr[start][1]:
            MIN = tmp + arr[start][1]
            return

    for i in range(2, N+2):
        if pick[i]:
            continue
        pick[i] = 1
        find(cnt+1, i, tmp + arr[start][i])
        pick[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    P = [(p[_], p[_+1]) for _ in range(0, len(p), 2)]
    arr = [[0]*(N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            if i != j:
                arr[i][j] = abs(P[i][0]-P[j][0]) + abs(P[i][1] - P[j][1])

    MIN = 0xfffffff
    pick = [0] * (N+2)


    for i in range(2, N+2):
        pick[i] = 1
        tmp = arr[0][i]
        find(1, i, tmp)
        pick[i] = 0

    print('#{} {}'.format(tc, MIN))