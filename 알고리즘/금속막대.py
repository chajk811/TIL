import sys
sys.stdin = open('금속막대_input.txt')

test_case = int(input())

for case in range(1, test_case+1):

    N = int(input())
    arr = list(map(int,input().split()))

    # 첫번째로 올 나사 찾기(전체리스트를 count 했을 때, 개수는 1개이며 앞에 나사의 앞에 위치함)
    p1, p2 = 0, 0

    for i in range(len(arr)):
        if arr.count(arr[i]) == 1 and i % 2 == 0:
            p1, p2 = arr[i], arr[i+1]
            arr[i], arr[i+1] = arr[0], arr[1]
            arr[0], arr[1] = p1, p2
            p1, p2 = 0, 0

    # 2번째 for문부터 끝날때까지 반복하면 된다.
    for i in range(2, len(arr), 2):
        p1, p2 = 0, 0
        for j in range(i,len(arr)-1):
            if arr[j] == arr[i-1]:
                p1, p2 = arr[j], arr[j+1]
                arr[j], arr[j+1] = arr[i], arr[i+1]
                arr[i], arr[i+1] = p1, p2

    result = ' '.join(map(str, arr))

    print('#{} {}'.format(case, result))
















