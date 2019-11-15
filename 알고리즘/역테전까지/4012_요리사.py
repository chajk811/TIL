import sys
import itertools
sys.stdin = open('4012_input.txt')

def check(nums):
    SUM = 0
    for num in nums:
        for i in nums:
            SUM += arr[num][i]
    return SUM


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    idx = [i for i in range(N)]

    # 조합
    pick = list(itertools.combinations(idx, N // 2))
    cnt = len(pick)
    MIN = 0xfffffff

    # check() & 비교
    for p in range(cnt // 2):
        A, B = pick[p], pick[cnt - 1 - p]
        SA, SB = check(A), check(B)
        tmp = abs(SA - SB)
        if MIN > tmp:
            MIN = tmp

    print('#{} {}'.format(tc, MIN))

