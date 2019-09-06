import sys
sys.stdin = open('5658_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    p = list(input())

    arr = []
    row = ''
    for j in range(N//4):
        p.insert(0, p.pop())
        for i in range(N):
            row += p[i]
            if len(row) == N//4:
                arr.append(row)
                row = ''

    for k in range(len(arr)):
        arr[k] = int(arr[k], 16)

    arr = list(set(arr))
    arr.sort(reverse=True)

    print('#{} {}'.format(tc, arr[K-1]))