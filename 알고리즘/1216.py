import sys
sys.stdin = open('1216_input.txt')


for i in range(1, 11):
    case = int(input())
    arr = []
    for i in range(100):
        arr.append(list(input()))

    # 회문 2는 길이가 정해져 있지 않음.
    # 길이가 줄어드는 방식으로
    # 시작 위치와 끝나는 위치를 정해놓고 생각하기
    ans = 1

    # 행검색
    for idx in range(100):
        for s in range(100):
            for e in range(99, s, -1):
                L = e - s + 1
                if ans >= L:
                    break
                for i in range(L//2):
                    if arr[idx][s+i] != arr[idx][e-i]:
                        break
                else:
                    ans = L

    # 늘려가는 방법
    for idx in range(100):
        for x in range(100):
            # 길이가 짝수인 경우에는 x -> l (왼쪽)
            l, r, cnt = x, x+1, 0
            while l >= 0 and r > 100:
                if arr[idx][l] != arr[idx][r]: break
                l -= 1
                r += 1
                cnt += 2