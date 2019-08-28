import sys
sys.stdin = open('최대합_최소합_input.txt')

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = []

    for i in range(N):
        arr.append(list(map(int,input().split())))

    print(arr)

    # MAX 값과 MIN 값을 따로 변수로 둬서 행과 열 대각선을 돌면서 확인하고 저장

    MAX = sum(arr[0])
    MIN = sum(arr[0])


    for i in range(len(arr)): # 행검사
        SUM = 0
        for j in range(len(arr[0])):
            SUM += arr[i][j]
        if SUM > MAX:
            MAX = SUM
        elif SUM < MIN:
            MIN = SUM

    for i in range(len(arr[0])):
        SUM = 0
        for j in range(len(arr)):
            SUM += arr[j][i]
        if SUM > MAX:
            MAX = SUM
        elif SUM < MIN:
            MIN = SUM

    left_top = 0
    right_top = 0

    for i in range(N):
        left_top += arr[i][i]
        right_top += arr[i][N-1-i]

    if left_top > MAX:
        MAX = left_top
    elif right_top > MAX:
        MAX = right_top
    elif left_top < MIN:
        MIN = left_top
    elif right_top < MIN:
        MIN = right_top

    print('#{} {}'.format(case, MAX-MIN))
