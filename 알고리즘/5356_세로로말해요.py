import sys
sys.stdin = open('5356_input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    L = 0
    for i in range(5):
        if L < len(arr[i]):
            L = len(arr[i])

    for i in range(5):
        if len(arr[i]) != L:
            while len(arr[i]) < L:
                arr[i].append(' ')

    result = ''
    for i in range(L):
        for j in range(5):
            if arr[j][i] != ' ':
                result += arr[j][i]

    print('#{} {}'.format(tc, result))


