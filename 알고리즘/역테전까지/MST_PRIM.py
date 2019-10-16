import sys; sys.stdin = open('mst_input.txt', 'r')

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

key = [0xfffff] * V      # 0 ~ V-1
pi = [0] * V
key[0] = 0

cnt = V
visit = [False] * V
while cnt:
    u = MIN = 0xffffff
    for i in range(V):
        if not visit[i] and MIN > key[i]:
            u, MIN = i, key[i]
    visit[u] = True

    for v, w in G[u]:
        if not visit[v] and w < key[v]:
            key[v], pi[v] = w, u

    cnt -= 1


for i in range(V):
    print(i, pi[i], key[i])
