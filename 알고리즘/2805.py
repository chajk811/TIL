import sys
sys.stdin = open('2805_input.txt')

def check(N):
    global c
    c = [0] * N

    for i in range(N):
        if i <= N//2:
            c[i] = (2*i) + 1
        else:
            c[i] = c[N-i-1]



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    c = [0] * N
    cnt = 0
    result = 0

    check(N)

    while cnt < N:
        j = c[cnt]
        s = (N-j) // 2

        for k in range(s, s+j):
            result += arr[cnt][k]

        cnt += 1


    print('#{} {}'.format(tc, result))



