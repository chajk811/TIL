import sys
sys.stdin = open('4366_input.txt')

d = [2, 1, -1, -2]

def change(n, p, num): # (입력받은 수, 가능한 숫자 저장할 리스트, 몇 진수)
    n = list(map(int, n[::-1]))

    for i in range(len(n)):
        tmp = n[i]
        for j in range(4):
            new = n[i] + d[j]
            SUM = 0
            if 0 <= new < num:
                n[i] = new
                for k in range(len(n)):
                    SUM += (num ** k) * n[k]
                else:
                    p.append(SUM)
                    n[i] = tmp


T = int(input())

for tc in range(1, T+1):
    n2 = input()
    n3 = input()
    p2 = []
    p3 = []

    change(n2, p2, 2)
    change(n3, p3, 3)

    print(p2)
    print(p3)

    result = 0

    for i in p2:
        if i in p3:
            result = i
            break

    print('#{} {}'.format(tc, result))