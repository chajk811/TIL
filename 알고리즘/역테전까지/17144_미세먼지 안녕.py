import sys
sys.stdin = open('17144_input.txt')

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move():
    global arr, air
    tmp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                tmp[i][j] = -1
                if len(air) != 2:
                    air.append(i)
            elif arr[i][j] > 0:
                x, y = i, j
                now = arr[i][j]
                cnt = 0
                for d in range(4):
                    nx = dx[d] + x
                    ny = dy[d] + y
                    if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                        tmp[nx][ny] += now // 5
                        cnt += 1
                tmp[x][y] += now - (now//5) * cnt
    arr = tmp

def delete():
    global arr




# 총 8개 tc
T = int(input())

for tc in range(1, T+1):
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    air = []


    for t in range(T):
        move()









# 공기청정기는 항상 왼쪽 열에 설치, 크기 두행을 차지
# 1초 동안 일이 순서대로 일어남

# <미세먼지>
# 모든 미세먼지에서 동시에, 인접한 네 방향으로 확산
# 확산되는 양 = 현재 미세먼지 // 5
# 확산후 남은 양 = 현재 미세먼지 - (확산되는 양) * 확산 방향

# <공기청정기 작동>
# 위쪽 공기청정기의 바람은 반시계방향으로 순환
# 아래 공기청정기의 바람은 시계방향
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한칸씩 이동


# 확산 전, 확산 후 두개의 리스트로
# 전에서 확인해서 미세먼지가 있으면 확산결과를 새 리스트에 저장







