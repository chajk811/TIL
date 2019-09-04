import sys
sys.stdin = open('2001_파리퇴치_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    SUM = 0
    MAX = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                for l in range(M):
                    SUM += arr[i+k][j+l]
            if MAX < SUM:
                MAX = SUM
            SUM = 0
    print('#{} {}'.format(tc, MAX))


