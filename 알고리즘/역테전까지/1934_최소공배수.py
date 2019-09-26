def find(A, B):
    global result
    tmp = min(A, B)
    fin = 0

    while fin == 0:
        for i in range(1, tmp + 1):
            if i == 1:
                continue
            if A % i == 0 and B % i == 0:
                A //= i
                B //= i
                result *= i
                break
        else:
            fin = 1
    return result * A * B

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())

    result = 1
    print(find(A, B))
