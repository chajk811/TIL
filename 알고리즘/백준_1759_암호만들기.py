L, C = 4, 6
arr = ['a', 't', 'c', 'i', 's', 'w']

# 암호는 최소 1개의 모음과 최소 2개의 자음으로 구성
# 알파벳 순서 선호?
# L: 암호 길이, C: 주어진 알파벳 개수

# 모음에서 하나뽑고
# 자음에서 두개 뽑고
# 뽑힌 모음 한개와 자음 두개는 표시하고
# 전체에서 표시 안된 것중에서 나머지 개수 뽑기

vowel = ['a', 'e', 'i', 'o', 'u']
picked = [0] * C
g1 = []
g2 = []

for ch in arr:
    if ch in vowel:
        g1.append(ch)
    else:
        g2.append(ch)
