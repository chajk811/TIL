import sys
sys.stdin = open('1486_input.txt')

# 부분 집합
def find():
    global S

    for i in range((1 << N) - 1):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += arr[j]
        if s >= B:
            if s == B:
                return 0
            elif S > s:
                S = s
    return S - B


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    S = sum(arr)

    print('#{} {}'.format(tc, find()))

