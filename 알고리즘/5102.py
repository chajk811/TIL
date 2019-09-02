import sys
sys.stdin = open('5102_input.txt')

## 1
def BFS(s):
    Q.append(s)
    visited[s] = 1

    while Q:
        now = Q.pop(0)
        for d in range(len(dir[now])):
            new = dir[now][d]
            if not visited[new]:
                Q.append(new)
                visited[new] = visited[now] + 1
                if new == g:
                    return


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split()) # V: 노드 수, E: 간선 수

    dir = [[] for _ in range(V+1)]

    for d in range(E):
        a, b = map(int, input().split())
        dir[b].append(a)
        dir[a].append(b)

    s, g = map(int, input().split())
    visited = [0] * (V+1)
    Q = []

    BFS(s)
    print('#{} {}'.format(tc,visited[g]-1))

## 2
# def BFS(s):
#     Q.append(s)
#     visited[s] = 1
#
#     while Q:
#         # print(Q)
#         now = Q.pop(0)
#         for d in range(len(dir[now])):
#             new = dir[now][d]
#             if not visited[new]:
#                 Q.append(new)
#                 visited[new] = 1
#                 D[new] = D[now] + 1
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     V, E = map(int, input().split()) # V: 노드 수, E: 간선 수
#
#     dir = [[] for _ in range(V+1)]
#
#     for d in range(E):
#         a, b = map(int, input().split())
#         dir[b].append(a)
#         dir[a].append(b)
#
#     s, g = map(int, input().split())
#     visited = [0] * (V+1)
#     Q = []
#     D = [0] * (V+1)
#
#     BFS(s)
#     print('#{} {}'.format(tc, D[g]))


##3
# T = int(input())

# def BFS(v,G):
#     global M
#     queue = []
#     queue.append(v)
#     visited = [0] * (V+1)
#     visited[v] = 1
#
#     while len(queue) != 0:
#         t = queue.pop(0)
#         for w in range(1, V+1):
#             if M[t][w] == 1 and visited[w] == 0:
#                 queue.append(w)
#                 visited[w] = visited[t] + 1
#                 if w == G:
#                     return visited[w] - 1
#     return 0
#
# for tc in range(T):
#     V, E = map(int,input().split())
#     M = [[0 for _ in range(V+1)] for _ in range(V+1)]
#     for _ in range(E):
#         k, v = map(int, input().split())
#         M[k][v] = 1
#         M[v][k] = 1
#
#     S, G = map(int, input().split())
#     print('#{} {}'.format(tc+1, BFS(S,G)))




