import sys
sys.stdin = open('섬문제_input.txt')

def move(x, y, dir):
    visit[x][y] = True
    result.append(arr[x][y])

    if dir == 1 and x - 1 >= 0:  # 상: 1, 우: 2, 하: 3, 좌: 4
        x, y = x - 1, y
    elif dir == 2 and y + 1 < N:
        x, y = x, y + 1
    elif dir == 3 and x + 1 < N:
        x, y = x + 1, y
    elif dir == 4 and y - 1 >= 0:
        x, y = x, y - 1

    move(x, y, dir)

T = int(input())

for case in range(1, T+1):
    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))

    print(arr)

    # 0 -> 바다, 1이상 -> 섬
    # 이어져있는 섬을 찾고 섬 중에서 가장 높은 높이를 찾는다.
    # N X N 행렬의 인덱스 이용
    # 한개의 섬을 찾을때 리스트에 담는다? 돌아 다닐때 한번 방문한 곳이면 가지 않는다.

    visit = []
    for _ in range(N):
        visit.append([False] * N)

    # 처음 위치를 찾는다.

    x, y = 0, 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visit[i][j] == False:
                x, y = i, j
                break


    result = [] # 방문한 섬의 높이
    dir = 0


    
    