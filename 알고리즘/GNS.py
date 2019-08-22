import sys
sys.stdin = open('GNS_test_input.txt')

## 1
# T = int(input())
#
# for i in range(1, T+1):
#     case, N = map(str, input().split())
#     N = int(N)
#     arr = list(map(str, input().split()))
#
#     new_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     new_num_count = ['']*10
#     NIN = 0
#
#     for i in range(N):
#         if arr[i] == new_num[9]:
#             NIN += 1
#         if new_num.index(arr[i]) == 9 and NIN == arr.count("NIN"):
#             new_num_count[new_num.index(arr[i])] += arr[i]
#         else:
#             new_num_count[new_num.index(arr[i])] += arr[i] + ' '
#
#     print('{} {}'.format(case, ''.join(new_num_count)))


## 2
# T = int(input())
#
# for i in range(1, T+1):
#     case, N = map(str, input().split())
#     N = int(N)
#     arr = list(map(str, input().split()))
#
#     new_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     new_num_count = [0]*10
#
#     for i in range(N):
#         new_num_count[new_num.index(arr[i])] += 1
#
#     result = ''
#
#     for i in range(10):
#         for j in range(new_num_count[i]):
#             if i == 9 and j == new_num_count[i]-1:
#                 result += new_num[i]
#             else:
#                 result += new_num[i] + ' '
#
#     print('{} {}'.format(case, result))