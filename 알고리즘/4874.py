import sys
sys.stdin = open('4874_input.txt')

T = int(input())

for case in range(1, T+1):
    arr = list(map(str, input().split()))

    S = []
    oper = ['+', '-', '/', '*']

    for ch in arr:
        if ch.isdigit():
            S.append(ch)
        if ch in oper:
            if len(S) < 2:
                print('#{} error'.format(case))
                break
            p1 = int(S.pop())
            p2 = int(S.pop())
            if ch == '+':
                p3 = p2 + p1
            elif ch == '-':
                p3 = p2 - p1
            elif ch == '/':
                p3 = p2 // p1
            elif ch == '*':
                p3 = p2 * p1
            S.append(p3)
        if ch == '.':
            if len(S) == 1:
                print('#{} {}'.format(case, S.pop()))
            else:
                print('#{} error'.format(case))

