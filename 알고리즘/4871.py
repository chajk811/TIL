import sys
sys.stdin = open('4871_input.txt')

def my_DSF(v):
    s = []
    visit = [False] * (V+1)
    visit[v] = True
    s.append(v)
    while s:
        for w in arr[v]:
            if not visit[w]:
                visit[w] = True
                s.append(v)
                v = w

                if w == G:
                    return 1
                break
        else:
            v = s.pop()
    return 0

T = int(input())
for case in range(1, T+1):

    V, E = map(int,input().split())
    arr = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int,input().split())
        arr[u].append(v)

    S, G = map(int, input().split())
    print(arr)

    print('#{} {}'.format(case, my_DSF(S)))