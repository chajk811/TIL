# 계산기

arr = '2+3*4/5'
S = []
result = []

# i.isdigit()
# 우선 순위 +- < /*
# oper1 = ['+', '-']
# oper2 = ['/', '*']


for ch in arr:
    if ch.isdigit():
        result.append(ch)
    else:
        S.append(ch)
else:
    while S:
        result.append(S.pop())

print(''.join(result))

# for ch in result:
#     if ch.isdigit():
#         S.append(ch)
#     else:
#         n1 = S.pop()
#         n2 = S.pop()
#         n3 =