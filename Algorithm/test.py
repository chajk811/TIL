import sys
sys.stdin = open('test_input.txt')

cases = int(input())
for case in range(1, cases+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    # print(charge)

    station = [0] * (N+1)
    for i in charge:
        station[i] += 1
    # print(station)

    count = 0
    move = K

    for j in range(len(station)):
        if j == N or j+move >= N:
            # 남은 move 수로 도착했을 때 그곳이 마지막 이면 break
            break
        if station[j] == 0 and move == 0:
            count = 0
            break
        if station[j] == 1:
            if move == 0:
                move = K
                count += 1
            else:
                a = []
                for k in range(1, move+1):
                    a.append(station[j+k])

                if 1 in a:
                    pass
                else:
                    move = K
                    count += 1
        move -= 1

    print('#%d %d' %(case, count))