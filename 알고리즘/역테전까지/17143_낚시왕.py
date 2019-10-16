import sys
sys.stdin = open('17143_input.txt')

T = int(input())

for tc in range(1, T+1):
    R, C, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    print(arr)

