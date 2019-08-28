import sys
sys.stdin = open('4875_input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    global ans
    S.append((x, y))
    visit[x][y] = 1

    while S:
        x, y = S.pop()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny <N and visit[nx][ny] == 0:
                if arr[nx][ny] == 2:
                    ans = 1
                    return
                if arr[nx][ny] == 0:
                    S.append((nx, ny))
                    visit[nx][ny] = 1

def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                DFS(i,j)
                return

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for i in range(N)]

    S = []
    visit = [[0]*N for _ in range(N)]
    ans = 0

    find()

    print('#{} {}'.format(case, ans))











# # DFS
# SIZE = 100
#
#
# dy = (-1,1,0)
# dx = (0,0,-1)
#
# def DFS(i,j):
#     Stack = [(i,j,2)]
#
#     while len(Stack)>0:
#         x, y, d = Stack.pop()
#
#         if x == 0:
#             return y
#
#         if d != 2:
#             while M[x][y] == 0:
#                 x = dx[d] + x
#                 y = dy[d] + y
#
#
#         for m in range(3):
#             if d == 1 and m == 0:
#                 continue
#             elif d == 0 and m == 1:
#                 continue
#             nx = dx[m] + x
#             ny = dy[m] + y
#             if 0 <= nx < SIZE and 0<=ny<SIZE:
#                 if M[nx][ny] == 1:
#                     Stack.append((nx,ny,m))
#                     break
#
#
# def getStart():
#     for i in range(SIZE-1, -1,-1):
#         for j in range(SIZE-1,-1,-1):
#             if M[i][j] == 2:
#                 return DFS(i,j)
#
#
#
#
# for tc in range(10):
#     t = input()
#     M = [list(map(int, input().split())) for _ in range(SIZE)]
#
#     print(f"#{tc+1} {getStart()}")

## BFS
# SIZE = 100
#
#
# dy = (-1,1,0)
# dx = (0,0,-1)
#
# def BFS(i,j):
#     Q = [(i,j,2)]
#
#     while len(Q)>0:
#         x, y, d = Q.pop(0)
#
#         if x == 0:
#             return y
#
#         if d != 2:
#             while M[x][y] == 0:
#                 x = dx[d] + x
#                 y = dy[d] + y
#
#
#         for m in range(3):
#             if d == 1 and m == 0:
#                 continue
#             elif d == 0 and m == 1:
#                 continue
#             nx = dx[m] + x
#             ny = dy[m] + y
#             if 0 <= nx < SIZE and 0<=ny<SIZE:
#                 if M[nx][ny] == 1:
#                     Q.append((nx,ny,m))
#                     break
#
#
# def getStart():
#     for i in range(SIZE-1, -1,-1):
#         for j in range(SIZE-1,-1,-1):
#             if M[i][j] == 2:
#                 return BFS(i,j)
#
#
#
#
# for tc in range(10):
#     t = input()
#     M = [list(map(int, input().split())) for _ in range(SIZE)]
#
#     print(f"#{tc+1} {getStart()}")