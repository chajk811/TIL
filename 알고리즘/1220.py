import sys
import pprint
sys.stdin = open('1220_input.txt')

for case in range(1, 11):
    N = int(input())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 행 검색
    # N극 : 1, S극 : 2
    # 1이 먼저 나오고 2가 나오면 고착상태, result == 3 인 경우
    # 카운트 수 += 1

    count = 0

    for i in range(len(arr[0])):
        result = 0

        for j in range(len(arr)):
            if result == 0 and arr[j][i] == 1:
                result += 1

            if result == 1 and arr[j][i] == 2:
                result = 0
                count += 1
    print('#{} {}'.format(case, count))

