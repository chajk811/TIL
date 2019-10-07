# 재귀
def fibo(n):
    global cnt
    cnt += 1

    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# 메모이제이션
def fibo_memo(n):
    global cnt_memo
    cnt_memo += 1

    if n >= 2 and memo[n] == -1:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]

# 또 다른 DP 방법
def fibo_dp(n):
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1]+memo[i-2]
    return memo[n]

N = int(input())
memo = [-1] * (N+1)
memo[0] = 0
memo[1] = 1
cnt = 0
cnt_memo = 0


print('피보나치 결과:', fibo(N))
print('호출횟수:', cnt)
print('-----')
print(fibo_memo(N))
print(cnt_memo)
print(memo)

