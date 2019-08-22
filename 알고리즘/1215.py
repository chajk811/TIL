import sys
sys.stdin = open('1215_input.txt')

for case in range(1, 11):
    N = int(input())
    arr = []

    for i in range(8):
        arr.append(list(input()))


    count = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])-N+1):
            if arr[i][j] == arr[i][j+N-1]:
                for k in range(N//2):
                    if arr[i][j+k] != arr[i][j+N-k-1]:
                        break
                else:
                    count += 1

    for i in range(len(arr[0])):
        for j in range(len(arr)-N+1):
            if arr[j][i] == arr[j+N-1][i]:
                for k in range(N//2):
                    if arr[j+k][i] != arr[j+N-k-1][i]:
                        break
                else:
                    count += 1

    print('#{} {}'.format(case, count))


# [
# ['C', 'B', 'B', 'C', 'B', 'A', 'A', 'B'],
# ['C', 'C', 'C', 'B', 'A', 'B', 'C', 'B'],
# ['C', 'A', 'A', 'A', 'A', 'C', 'A', 'B'],
# ['B', 'A', 'C', 'C', 'C', 'C', 'A', 'C'],
# ['A', 'A', 'B', 'C', 'B', 'B', 'A', 'C'],
# ['A', 'C', 'A', 'A', 'C', 'A', 'B', 'C'],
# ['B', 'C', 'C', 'B', 'A', 'A', 'B', 'C'],
# ['A', 'B', 'B', 'B', 'C', 'C', 'A', 'A']
# ]

