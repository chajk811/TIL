import sys
sys.stdin = open('1979_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 검사
    # 열 검사

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                S = 1
                for k in range(j+1, N):
                    if arr[i][k] == 0:
                        break
                    if j == 0:
                        if arr[i][k] == 1:
                            S += 1
                    elif arr[i][j-1] != 1 and arr[i][k] == 1:
                        S += 1
                if S == M:
                    cnt += 1


    for i in range(N):
        for j in range(N):
            if arr[j][i] == 1:
                S = 1
                for k in range(j+1, N):
                    if arr[k][i] == 0:
                        break
                    if j == 0:
                        if arr[k][i] == 1:
                            S += 1
                    elif arr[j-1][i] != 1 and arr[k][i] == 1:
                        S += 1
                if S == M:
                    cnt += 1


    print('#{} {}'.format(tc, cnt))

