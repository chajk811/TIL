import sys
sys.stdin = open('4014_input.txt')

def find():
    global cnt

    for i in range(N):
        tmp = arr[i][0]
        for j in range(N):
            if arr[i][j] != tmp:
                if check(i, j):
                    cnt += 1
                    tmp = arr[i][j]
                else:
                    break


def check(x, y): # 0 또는 1 return

    if y+M







T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
