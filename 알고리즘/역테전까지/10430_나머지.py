A, B, C = map(int, input().split())
# A, B, C = 5, 8, 4

print((A + B) % C)
print((A % C + B % C) % C)
print((A * B) % C)
print((A % C * B % C) % C)
