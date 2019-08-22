import sys
sys.stdin = open('4869_input.txt')

def my_func(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return my_func(n-1) + my_func(n-2) * 2

T = int(input())

for case in range(1, T+1):
    N = int(input())

    print('#{} {}'.format(case, my_func(N//10)))





