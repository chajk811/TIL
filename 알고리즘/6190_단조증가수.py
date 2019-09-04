import sys
sys.stdin = open('6190_단조증가수_input.txt')

def comb(cnt, S, N, result): # cnt: 뽑는 횟수 체크, S: 시작위치, N: 뽑아야하는 배열의 길이, result: 결과값 비교용
    global MAX

    if cnt == 2:
        print(result)
        # 단조 증가 수 인지 확인
        # 맞다면 result와 비교해서 큰 수 입력

        a = str(result)
        for i in range(len(a)-1):
            if int(a[i]) > int(a[i+1]):
                break
        else:
            if MAX < int(a):
                MAX = int(a)
        return

    for i in range(S, N):
        if pick[i] == 0:
            pick[i] = 1
            comb(cnt+1, i+1, N, result * arr[i])
            pick[i] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    MAX = 0
    pick = [0] * N
    # 조합으로 곱 확인
    comb(0, 0, N, 1)

    if MAX:
        print('#{} {}'.format(tc, MAX))
    else:
        print('#{} -1'.format(tc))

