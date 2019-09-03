import sys
sys.stdin = open('5108_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    add = [list(map(int, input().split())) for _ in range(M)]

    for i in add:
        arr.insert(i[0], i[1])

    print('#{} {}'.format(tc, arr[L]))
