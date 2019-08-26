import sys
sys.stdin = open('1267_input.txt')

for case in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    print(arr)

    # 받는 간선의 개수가 0인 것부터 없애기
    # 시작해서 쭉 따라가고 끝이나면 다음 0을 찾기

    count = [0] * (V+1)

    for i in range(1, len(arr), 2):
            count[arr[i]] += 1
    print(count)

    pick = 0
    for i in range(1, len(count)):
        if i == 0:
            pick = i
            break

    # pick 번째의 요소부터 지워나가면 됨
    # 화살표 정보 필요

    dir = []
