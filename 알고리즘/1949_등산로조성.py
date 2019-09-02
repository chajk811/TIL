import sys
sys.stdin = open('1949_등산로조성.txt')

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# top 리스트를 돌면서 DFS로 탐색
# S에 지나가는 [x,y] 를 쌓아가며
# cnt 라는 변수를 둬서 이동하는 횟수를 측정

def DFS(tmp):
    global cnt
    x, y = tmp
    S.append([x, y])
    visited[x][y] = 1

    while S:
        x, y = S.pop()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[x][y] > arr[nx][ny]:
                    S.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                    # if visited_max < visited[nx][ny]:
                    #     visited_max = visited[nx][ny]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 3 ≤ N ≤ 8
    # 1 ≤ K ≤ 5
    # 지형의 높이는 1 이상 20 이하의 정수
    # 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

    # 최대 높이 지점 찾기 [x, y]
    top = []
    h = 0
    for m in range(20, 0, -1):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == m:
                    top.append([i, j])
                    h = m
        if top:
            break

   # DFS로 탐색, 시작점의 x,y 좌표를 입력
   # cnt 라는 변수를 두고 시작점을 이동해가면서
   # 비교해서 큰 수로 교체해준다

   # cnt_max = 0
   #
   # for t in range(len(top)):
   #     S = []
   #     visited = [[0]*N for _ in range(N)]
   #     cnt = 0
   #
   #     DFS(top[t])
   #
   #     if cnt_max < cnt:
   #         cnt_max = cnt
   #
   #  print('#{} {}'.format(tc, cnt_max))

    cnt_max = 0

    S = []
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    DFS(top[0])
    print(visited)

    # print(visited_max)
    # visited_max_tmp = []
    #
    # for a in range(N):
    #     for b in range(N):
    #         if visited[a][b] == visited_max:
    #             visited_max_tmp.append([a, b])
    # print(visited_max_tmp)
    #
    # for c in visited_max_tmp:
    #     DFS(c)
