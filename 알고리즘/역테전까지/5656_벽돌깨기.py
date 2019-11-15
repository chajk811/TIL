import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('5656_input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def ball(times, total_brick):
    global result, arr
    if times == N:
        result == min(result, total_brick)
        return

    Q = deque()

T = int(input())

for tc in range(1, T+1):
    result = 0xfffffff
    N, W, H = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(H)]
    total_brick = W * H
    pick = []

    for i in range(H):
        total_brick -= origin[i].count(0)

    arr = deepcopy(origin)
    ball(0, total_brick)

