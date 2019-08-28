arr = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7
line = [[] for _ in range(N+1)]
Q = []
visit = [0] * (N+1)

for i in range(0, len(arr), 2):
    line[arr[i]].append(arr[i+1])
    line[arr[i+1]].append(arr[i])

print(line)

def BFS(n):
    Q.append(n)
    visit[n] = 1

    while len(Q) > 0:
        n = Q.pop(0)
        print(n)
        for d in range(len(line[n])):
            new_n = line[n][d]
            if visit[new_n] == 0:
                Q.append(new_n)
                visit[new_n] = 1

BFS(1)






