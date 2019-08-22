import sys
sys.stdin = open('초심자의회문_input.txt')

T = int(input())
for case in range(1, T + 1):
    words = input()
    result = 0

    for i in range(len(words) // 2):
        if words[i] != words[len(words) - 1 - i]:
            result = 0
            break
        else:
            result = 1

    print('#{} {}'.format(case, result))