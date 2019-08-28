import sys
sys.stdin = open('4881_input.txt')

def DFS(n, count):
    global MIN
    if count > MIN:
        return

    if n == N:
        if count < MIN:
            MIN = count
        return
    for i in range(N):
        if not tmp[i]:
            tmp[i] = 1
            DFS(n+1, count+M[n][i])
            tmp[i] = 0


T = int(input())
for tc in range(T):
    N = int(input())

    M = [list(map(int,input().split())) for _ in range(N)]
    tmp = [0]*N
    MIN = 0xfffffff
    DFS(0, 0)

    print("#{} {}".format(tc+1, MIN))



# def perm(k, n):
#     if k == n:
#         pick = ''.join(list(map(str, order)))
#         result.append(pick)
#         return
#     for i in range(n):
#         if used[i]: continue
#
#         used[i] = True
#         order.append(numbers[i])
#
#         perm(k+1, n)
#
#         used[i] = False
#         order.pop()
#
# T = int(input())
#
# for case in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # print(arr)
#
#     # 열이 중복이 안되도록 순열로 뽑는다.
#     # 행을 바꿔가면서 순열의 숫자를 순서대로 사용
#     # 합을 구하고 MIN값과 비교하여 최소값을 구한다.
#
#     numbers = [_ for _ in range(N)]
#     used = [False] * N
#     order = []
#     result = []
#
#     perm(0, N)
#     # print(result)
#
#     MIN = 100
#
#     for ch in result:
#         SUM = 0
#         for i in range(N): # 행과, 순열로 뽑아진 열의 인덱스를 같이 바꿔줌
#             SUM += arr[i][int(ch[i])]
#         if SUM < MIN:
#             MIN = SUM
#
#     print('#{} {}'.format(case, MIN))


# def perm(k, n):
#     if k == n:
#         global MIN
#         pick = ''.join(list(map(str, order)))
#         SUM = 0
#
#
#         return
#
#     for i in range(n):
#         if used[i]: continue
#
#         used[i] = True
#         order.append(numbers[i])
#
#         perm(k + 1, n)
#
#         used[i] = False
#         order.pop()
#
#
# T = int(input())
#
# for case in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     numbers = [_ for _ in range(N)]
#     used = [False] * N
#     order = []
#     MIN = 100
#
#     perm(0, N)
#     print('#{} {}'.format(case, MIN))