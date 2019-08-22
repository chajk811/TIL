import sys
sys.stdin = open('4865_input.txt')

T = int(input())

for case in range(1, T+1):
    str1 = input()
    str2 = input()
    alpha = list(set(str1))
    count = [0]*len(alpha)

    for i in range(len(str2)):
        if str2[i] in alpha:
            count[alpha.index(str2[i])] += 1

    print('#{} {}'.format(case, max(count)))

