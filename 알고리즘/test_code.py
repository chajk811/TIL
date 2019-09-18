import sys
sys.stdin = open('1865_input.txt')

def process(s, cnt):
    global MAX

    if s * 100 <= MAX:
        return

    if cnt == N:
        if s * 100 > MAX:
            MAX = s * 100
        return

    for i in range(N):
        if chk[i] == 0:
            chk[i] = 1
            process(s * arr[cnt][i], cnt + 1)
            chk[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    chk = [0] * N
    MAX = 0

    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100

    process(1.0, 0)
    print('#%d %.6f' %(tc, MAX))