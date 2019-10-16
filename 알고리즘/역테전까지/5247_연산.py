import sys
sys.stdin = open('5247_input.txt')



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    MIN = 0xfffff


