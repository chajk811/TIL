import sys
sys.stdin = open('6485_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    P_arr = [int(input()) for _ in range(P)]
    B = [0] * (5001)

    for i in range(len(arr)):
        for j in range(arr[i][0], arr[i][1]+1):
                B[j] += 1


    result = []

    for i in P_arr:
        result.append(str(B[i]))

    print('#{} {}'.format(tc, ' '.join(result)))