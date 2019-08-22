import sys
sys.stdin = open('4864_input.txt')

T = int(input())

for case in range(1, T+1):
    str2 = input()
    str1 = input()

    N = len(str1)
    M = len(str2)

    result = 0

    for i in range(N-M+1):
        if str1[i] == str2[0]:
            for j in range(M):
                if str2[j] != str1[i+j]:
                    break
            else:
                result = 1

    print('#{} {}'.format(case, result))
