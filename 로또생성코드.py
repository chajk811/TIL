import random

# T줄 구매 기준
T = int(input())

result = []

for i in range(T):
    tmp = []
    while len(tmp) < 6:
        lucky_num = random.randrange(1, 46)
        if lucky_num not in tmp:
            tmp.append(lucky_num)
    tmp.sort()
    result.append(tmp)
    tmp = []

for p in range(T):
    print(result[p])
