import sys
sys.stdin = open('5122_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    c = [list(input().split()) for _ in range(M)]


    # I: 추가
    # D: 삭제
    # C: 교체

    while M > 0:
        for i in range(len(c)):
            if c[i][0] == 'I':
                arr.insert(int(c[i][1]), int(c[i][2]))
            elif c[i][0] == 'D':
                arr.pop(int(c[i][1]))
            elif c[i][0] == 'C':
                arr[int(c[i][1])] = int(c[i][2])

            M -= 1
    if len(arr) > L:
        print('#{} {}'.format(tc, arr[L]))
    else:
        print('#{} -1'.format(tc))


