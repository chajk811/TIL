import sys
sys.stdin = open('1210_input.txt')

# def DFS(x, y):
#     if x == 0: return y
#
#     arr[x][y] = 0
#     if y-1 >= 0 and arr[x][y-1]:
#         return DFS(x, y-1)
#     elif y+1 < 100 and arr[x][y+1]:
#         return DFS(x, y+1)
#     else:
#         return DFS(x-1. y)



for i in range(1, 11):
    case = int(input())

    arr = [list(map(int,input().split())) for i in range(100)]

    x, y = 99, 0
    for i in range(100):
        if arr[99][i] == 2:
            y = i
            break

    ## 2
    # while x:
    #     if y-1 >= 0 and arr[x][y-1]:
    #         while y-1 >= 0 and arr[x][y-1]:
    #             y -= 1
    #         x -= 1
    #
    #     elif y+1 < 100 and arr[x][y+1]:
    #         while y+1 < 100 and arr[x][y+1]:
    #             y += 1
    #         x -= 1
    #
    #     else:
    #         x -= 1
    #
    # print(y)

