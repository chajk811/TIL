import sys
sys.stdin = open('6109_input.txt')

def move(N, S):

    if S == 'left':
        for i in range(N):
            S = []
            result = [0] * N
            idx = 0

            for j in range(N):
                if arr[i][j] != 0:
                    S.append(arr[i][j])

            while len(S) > 0:
                if len(S) == 1:
                    result[idx] = S.pop()
                else:
                    pick1 = S.pop(0)
                    pick2 = S.pop(0)
                    if pick1 == pick2:
                        result[idx] = pick1 * 2
                        idx += 1
                    else:
                        result[idx] = pick1
                        S.insert(0, pick2)
                        idx += 1

            arr[i] = result

    if S == 'right':
        for i in range(N):
            S = []
            result = [0] * N
            idx = 0

            for j in range(N):
                if arr[i][j] != 0:
                    S.append(arr[i][j])

            while len(S) > 0:
                if len(S) == 1:
                    result[N-1-idx] = S.pop()
                else:
                    pick1 = S.pop()
                    pick2 = S.pop()
                    if pick1 == pick2:
                        result[N-1-idx] = pick1 * 2
                        idx += 1
                    else:
                        result[N-1-idx] = pick1
                        S.append(pick2)
                        idx += 1

            arr[i] = result

    if S == 'up':
        # 각 행 공백없이 뽑아서 S에 저장
        for i in range(N):
            S = []
            result = [0] * N
            idx = 0
            for j in range(N):
                if arr[j][i] != 0:
                    S.append(arr[j][i])

            # 스택에서 처음부터 뽑으면서 비교
            while len(S) > 0:
                if len(S) == 1:
                    result[idx] = S.pop()
                else:
                    pick1 = S.pop(0)
                    pick2 = S.pop(0)
                    if pick1 == pick2:
                        result[idx] = pick1 * 2
                        idx += 1
                    else:
                        result[idx] = pick1
                        S.insert(0, pick2)
                        idx += 1

            # result를 원래 arr로 바꿔주기
            for k in range(N):
                arr[k][i] = result[k]

    if S == 'down':
        for i in range(N):
            S = []
            result = [0] * N
            idx = 0
            for j in range(N):
                if arr[j][i] != 0:
                    S.append(arr[j][i])

            while len(S) > 0:
                if len(S) == 1:
                    result[N-1-idx] = S.pop()
                else:
                    pick1 = S.pop()
                    pick2 = S.pop()
                    if pick1 == pick2:
                        result[N-1-idx] = pick1 * 2
                        idx += 1
                    else:
                        result[N-1-idx] = pick1
                        S.append(pick2)
                        idx += 1

            for k in range(N):
                arr[k][i] = result[k]


T = int(input())

for tc in range(1, T+1):
    N, S = map(str, input().split())
    N = int(N)
    arr = [list(map(int, input().split())) for _ in range(N)]

    move(N, S)

    print('#{}'.format(tc))
    for _ in range(N):
        print(' '.join(list(map(str, arr[_]))))