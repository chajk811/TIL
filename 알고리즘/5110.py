import sys
sys.stdin = open('5110_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    result = []
    cnt = 1

    for i in range(N):
        result.append(arr[0][i])

    while cnt < len(arr):
        tmp = 0

        # 처음으로 찾은 큰 수가 있으면 그 수의 인덱스를 tmp에
        # 큰 수가 없다면 for문을 다돌고 tmp == 0
        for t in range(len(result)):
            if result[t] > arr[cnt][0]:
                tmp = t
                break
        else:
            tmp = -1

        if tmp == -1:
            for a in range(len(arr[cnt])):
                result.append(arr[cnt][a])
            cnt += 1
        else:
            for b in range(len(arr[cnt])):
                result.insert(tmp, arr[cnt][b])
                tmp += 1
            cnt += 1

    print('#{} {}'.format(tc, ' '.join(list(map(str, result[:-11:-1])))))