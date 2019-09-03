import sys
sys.stdin = open('5120_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    # 첫번째 생성위치 이동
    tmp = M

    while K > 0:
        if tmp == 0:
            arr.insert(0, arr[-1]+arr[0])
        elif tmp == len(arr):
            arr.append(arr[-1]+arr[0])
        else:
            arr.insert(tmp, arr[tmp-1]+arr[tmp])

        if tmp+M > len(arr):
            tmp = tmp+M-len(arr)
            K -= 1
        else:
            tmp += M
            K -= 1
    print(arr)

    if len(arr) > 10:
        print('#{} {}'.format(tc, ' '.join(list(map(str, arr[:-11:-1])))))
    else:
        print('#{} {}'.format(tc, ' '.join(list(map(str, arr[::-1])))))

# 전 [958, 386, 715, 329, 498, 667, 169, 778, 2514, 1736]
# 후 [1736, 2514, 778, 169, 667, 498, 329, 715, 386, 958]
