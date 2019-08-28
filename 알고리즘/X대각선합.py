import sys
sys.stdin = open('X대각선합_input.txt')

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())

    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 움직일 수 있는 범위 설정 K x K 행렬이 움직임
    # 위의 범위를 움직이면서 대각선의 합 확인, 차이를 MAX에 저장

    MAX = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            left, right = 0, 0
            for k in range(M):
                left += arr[i+k][j+k]
                right += arr[i+k][j+M-1-k]

            if MAX < abs(left-right):
                MAX = abs(left-right)
    print('#{} {}'.format(case, MAX))
