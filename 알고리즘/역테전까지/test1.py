import sys
sys.stdin = open('test1_input.txt')

t = int(input())

for tc in range(1, t+1):
    alpha = [list(input()) for _ in range(5)]
    result = ""

    for r in range(15):
        for c in range(5):
            if r < len(alpha[c]):
                result += alpha[c][r]

    print("#{} {}".format(tc, result))


# A A B C D D
# a f z z
# 0 9 1 2 1
# a 8 E W g 6
# P 5 h 3 k x
#
# Aa0aP/Af985/Bz1Eh/Cz2W3/D1gk/D6x