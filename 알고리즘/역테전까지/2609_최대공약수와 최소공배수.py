N, M = map(int, input().split())

# N, M = 24, 18

# 두 개의 수 중에서 작은값 만큼 for문을 돈다.
# 돌면서 두 수를 나눴을 때 나머지가 0 이 되면 나눠주고 break

gcd = 1 # 최대공약수
lcm = 1 # 최소공배수


def find(N, M):
    global gcd
    fin = 0

    while fin == 0 :
        tmp = min(N, M)
        for i in range(1, tmp + 1):
            if i == 1:
                continue
            if N % i == 0 and M % i == 0:
                N //= i
                M //= i
                gcd *= i
                break
        else:
            fin = 1
    return N, M

N, M = find(N, M)
lcm = gcd * N * M

print(gcd)
print(lcm)

