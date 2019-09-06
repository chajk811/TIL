import sys
sys.stdin = open('1974_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = 1

    S = []

    # 행 검사
    for i in range(N):
        for j in range(N):
            if arr[i][j] not in S:
                S.append(arr[i][j])
            else:
                check = 0
                break
        if check == 0:
            break
        S = []
    if check == 0:
        print('#{} 0'.format(tc))
        continue


    # 열 검사
    S = []
    for i in range(N):
        for j in range(N):
            if arr[j][i] not in S:
                S.append(arr[j][i])
            else:
                check = 0
                break
        if check == 0:
            break
        S = []
    if check == 0:
        print('#{} 0'.format(tc))
        continue


    # 사각 검사
    for i in range(3):
        for j in range(3):
            s_r = i * 3 # 행의 시작 위치
            s_c = j * 3 # 열의 시작 위치
            S = []
            for k in range(s_r, s_r+3):
                for m in range(s_c, s_c+3):
                    if arr[k][m] not in S:
                        S.append(arr[k][m])
                    else:
                        check = 0
                        break
                if check == 0:
                    break
            if check == 0:
                break
        if check == 0:
            break
    if check == 0:
        print('#{} 0'.format(tc))
        continue

    print('#{} {}'.format(tc, check))

