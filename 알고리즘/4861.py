import sys
sys.stdin = open('4861_input.txt')

T = int(input())

for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = []

    for i in range(N):
        arr.append(list(input()))

    result = []

    # 행 검색
    for i in range(len(arr)):
        # 행의 요소를 돌면서 확인(M 전까지)
        for j in range(len(arr[0])-M+1):
            if arr[i][j] == arr[i][j+M-1]:
                # 첫 번째가 마지막 이랑 같다면 확인, 반절 확인한다.
                for k in range(M//2):
                    if arr[i][j+k] != arr[i][M+j-k-1]:
                        break
                else:
                    for _ in range(j, j+M):
                        result.append(arr[i][_])

    for i in range(len(arr[0])):
        for j in range(len(arr)-M+1):
            if arr[j][i] == arr[j+M-1][i]:
                for k in range(M//2):
                    if arr[j+k][i] != arr[M+j-k-1][i]:
                        break
                else:
                    for _ in range(j, j+M):
                        result.append(arr[_][i])

    print('#{} {}'.format(case, ''.join(result)))