def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print('시작')
print(fibonacci(10))
print('끝')