import sys
sys.stdin = open('2005_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*i for i in range(1, N+1)]
    # print(arr)

    for j in range(N):
        for k in range(len(arr[j])):
            if k == 0 or k == len(arr[j]) - 1:
                arr[j][k] = 1
            else:
                if j > 1:
                    arr[j][k] = arr[j-1][k-1] + arr[j-1][k]

    print('#{}'.format(tc))
    for s in arr:
        print(' '.join(map(str, s)))
