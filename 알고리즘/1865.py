import sys
sys.stdin = open('1865_input.txt')

def perm(cnt, tmp): # (깊이, 현재까지 곱)
    global MAX

    if tmp <= MAX:
        return

    if cnt == N:
        if tmp > MAX:
            MAX = tmp
        return

    for i in range(N):
        if pick[i] == 0:
            # if arr[cnt][i] == 0:
            #     continue
            pick[i] = 1
            perm(cnt+1, tmp * arr[cnt][i])
            pick[i] = 0


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    MAX = 0
    pick = [0] * N

    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100


    perm(0, 1)

    print('#%d %.6f' %(tc, MAX*100))