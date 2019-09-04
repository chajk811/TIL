import sys
sys.stdin = open('4615_input.txt')

# 상부터 시계방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# 현재 위치에서 대각선으로 탐색할 수 있는 개수를 정하기 위한 함수
# 상 우 하 좌 순으로 두개씩 비교했을 때 그 가운데 대각선의 최대 길이는
# 짧은 것을 채택한다.
def c(check):
    for i in range(0, 8, 2):
        if i == 6:
            if check[i] < check[0]:
                check[i + 1] = check[i]
            else:
                check[i + 1] = check[0]
        else:
            if check[i] < check[i+2]:
                check[i+1] = check[i]
            else:
                check[i+1] = check[i+2]

    return check

# arr 를 돌면서 바둑돌을 놓는다
# 상 우 하 좌 를 체크하고 c(check) 를 실행시켜 현재 위치에서 탐색할 수 있는 개수를 구한다.
# 8방향을 for 문으로 돌면서 탐색하는데 한번 이동시켜봤을 때,
# 범위안에 들면 탐색시작
# 탐색과정에서 check[d] 수를 tmp 에 저장 tmp를 -1 씩 줄여가면서 횟수제한
# 탐색하는 동안 다음 위치가 B[nx][ny] == 0 이면 탐색중지
def play():
    for i in range(M):
        x, y = arr[i][0], arr[i][1]
        B[x][y] = arr[i][2]

        check = [x-1, 0, N-y, 0, N-x, 0, y-1, 0]
        check = c(check)

        for d in range(8):
            nx = dx[d] + x
            ny = dy[d] + y
            tmp = check[d]
            move = 0
            find = 0

            if 1 <= nx <= N and 1 <= ny <= N:
                while tmp > 0 and B[nx][ny] != 0:
                    tmp -= 1
                    if B[nx][ny] == arr[i][2]:
                        find = 1
                        break
                    else:
                        nx += dx[d]
                        ny += dy[d]
                        move += 1

                # 위에서 이어져 있는 방향으로 탐색했을때 같은색 바둑돌이 있으면
                # find = 1, 탐색 중지
                # x, y 처음 탐색 위치에서 그 방향으로 바꿔줌 (move 수만큼)
                if find == 1:
                    xx, yy = x, y
                    while move > 0:
                        xx += dx[d]
                        yy += dy[d]

                        B[xx][yy] = arr[i][2]
                        move -= 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    B = [[0]*(N+1) for _ in range(N+1)]

    for z in range(N//2, N//2+2):
        for w in range(N//2, N//2+2):
            if z == w:
                B[z][w] = 2
            else:
                B[z][w] = 1

    play()

    cnt1 = 0
    cnt2 = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if B[i][j] == 1:
                cnt1 += 1
            elif B[i][j] == 2:
                cnt2 += 1

    print('#{} {} {}'.format(tc, cnt1, cnt2))


