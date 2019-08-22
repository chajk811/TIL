import sys
sys.stdin = open('4839_input.txt')

test_case = int(input())

for case in range(1, test_case+1):
    P, Pa, Pb = map(int, input().split())

    num_list = list(range(P))

    start = 0
    end = P - 1
    count_a = 0

    while start <= end:
        count_a += 1
        mid = start + (end - start)//2
        if mid == Pa-1:
            break
        elif mid > Pa-1:
            end = mid
        else:
            start = mid
    else:
        count_a = False

    start = 0
    end = P - 1
    count_b = 0

    while start <= end:
        count_b += 1
        mid = start + (end - start)//2
        if mid == Pb-1:
            break
        elif mid > Pb-1:
            end = mid
        else:
            start = mid
    else:
        count_b = False

    if count_a < count_b or count_b == False:
        print('#{} A'.format(case))
    elif count_a == count_b:
        print('#{} 0'.format(case))
    elif count_a > count_b or count_a == False:
        print('#{} B'.format(case))