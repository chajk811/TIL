S = []

def push(item):
    S.append(item)

def pop():
    return S.pop()

def isEmpty():
    return len(S) == 0

paren = '()()((()))'

for ch in paren:
    if ch == '(':
        push(ch)
    else:
        if isEmpty():
            break
        if ch == ')' and pop() != '(':
            break
