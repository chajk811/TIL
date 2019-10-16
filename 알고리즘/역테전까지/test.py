import sys
sys.stdin = open('test_input.txt')

T = 1
for tc in range(1, T+1):
   N = int(input())
   arr = [list(map(int, input().split())) for _ in range(N)]
   ax = bx = cx = ay = by = cy = 0
   resultx = resulty = result = 0xfffff
   for i in range(0, N-2):
       for j in range(i+1, N-1):
           for k in range(N):
               ax += sum(arr[k][0:i + 1])
               bx += sum(arr[k][i + 1:j + 1])
               cx += sum(arr[k][j + 1:N])
           MAXx = max(ax, bx, cx)
           MINx = min(ax, bx, cx)
           if MAXx - MINx <= resultx:
               resultx = MAXx - MINx
           ax = bx = cx = 0

           # 0 ~ i, i+1 ~ j, j+1 ~ N-1

           for k in range(N):
               if k <= i:
                   ay += sum(arr[k])
               elif i+1 <= k < j+1:
                   by += sum(arr[k])
               else:
                   cy += sum(arr[k])
           ay, by, cy = 0, 0, 0
