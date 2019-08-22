import sys
sys.stdin = open('4873_input.txt')

T = int(input())

def change(words):
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            words.pop(i)
            words.pop(i)
            break
    else:
        return len(words)
    return change(words)

for case in range(1, T+1):
    words = list(input())

    print('#{} {}'.format(case, change(words)))

