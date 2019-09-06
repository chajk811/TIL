import sys
sys.stdin = open('5656_input.txt')

# 좌 우 상 하
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# cnt: 깊이, result: 그 횟수에서 깨진 벽돌의 수
# global MAX와 비교해서 아니면 재귀 return
# 깨뜨리고 재귀 호출하고 다시 원상복구

def DFS(cnt, result):
    global MAX

    if result > MAX:
        MAX = result
    else:
        return
    if cnt == N:
        return

    # 떨어 뜨릴 위치 처음부터 끝까지 바꿔가면서 확인
    for i in range(W):
        # 떨어 뜨리는 위치(열)의 가장 높은 행을 찾는다
        x, y = i, 0
        for j in range(H):
            if arr[j][i] != 0:
                y = j
                break

        # 다 삭제하고 깨지는 벽돌수+
        # 호출
        # 원상복구






T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split()) # W: 열, H: 행
    arr = [list(map(int, input().split())) for _ in range(H)]

    print(arr)

    # N번 구슬을 떨어뜨릴때 좌우로 움직일 수 있다.
    # DFS로 최대 깊이까지 확인해보고
    # 최대로 부쉈을때를 찾는다.

    # for 문으로 N 번 반복
    # for 문으로 W 번 반복

    MAX = -1
    DFS()