import sys
sys.stdin = open('1952_input.txt')

def find(cnt, tmp):
    global MIN

    if cnt >= 12:
        if tmp < MIN:
            MIN = tmp
        return

    if arr[cnt]:
        find(cnt + 1, tmp + P[0] * arr[cnt])
        find(cnt + 1, tmp + P[1])
        find(cnt + 3, tmp + P[2])
    else:
        find(cnt+1, tmp)


T = int(input())

for tc in range(1, T+1):
    P = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    MIN = P[3]

    find(0, 0)
    print('#{} {}'.format(tc, MIN))

