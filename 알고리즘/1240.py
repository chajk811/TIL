import sys
sys.stdin = open('1240_input.txt')

def check(i, j):
    tmp = ''

    if j+6 < M:
        for d in range(7):
            tmp += str(arr[i][j+d])
        if tmp in P:
            result.append(P[tmp])
    else:
        return

    if j+7 < M:
        if arr[i][j+7] == 1:
            check(i, j+7)
    else:
        return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, list(input())))[::-1] for _ in range(N)]
    result = []

    P = {
        '1011000': 0,
        '1001100': 1,
        '1100100': 2,
        '1011110': 3,
        '1100010': 4,
        '1000110': 5,
        '1111010': 6,
        '1101110': 7,
        '1110110': 8,
        '1101000': 9
    }

    for i in range(N):
        if 1 in arr[i]:
            for j in range(M):
                if arr[i][j] == 1:
                    check(i, j)
                    result = result[::-1]
                    break
            break

    SUM = 0
    for i in range(len(result)):
        if i % 2 == 0:
           SUM += result[i] * 3
        else:
            SUM += result[i]

    if SUM % 10 == 0:
        print('#{} {}'.format(tc, sum(result)))
    else:
        print('#{} 0'.format(tc))
