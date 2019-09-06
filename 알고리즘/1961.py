import sys
sys.stdin = open('1961_input.txt')

def turn():
    global arr

    tmp = []
    for i in range(N):
        column = []
        for j in range(N-1, -1, -1):
            column.append(arr[j][i])
        tmp.append(column)
    arr = tmp



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    result = [[0]*3 for _ in range(N)]

    for i in range(3):
        turn()
        for j in range(N):
            result[j][i] = ''.join(arr[j])

    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(result[i]))