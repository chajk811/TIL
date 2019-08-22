import sys
sys.stdin = open('4866_input.txt')


def push(item):
    S.append(item)


def pop():
    return S.pop()


def isEmpty():
    return len(S) == 0


T = int(input())
for case in range(1, T+1):
    words = input()

    S = []

    left = ['(', '{']
    right = [')', '}']
    result = 1

    for ch in words:
        if ch in left:
            push(ch)
        elif ch in right:
            if isEmpty():
                result = 0
                break
            if pop() != left[right.index(ch)]:
                result = 0
                break
    else:
        if isEmpty():
            result = 1
        else:
            result = 0

    print('#{} {}'.format(case, result))


