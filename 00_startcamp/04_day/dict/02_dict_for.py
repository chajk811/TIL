# 딕셔너리 반복문 활용하기

lunch = {
    '중국집': '02-111-1111',
    '분식집': '031-111-1111',
    '일식집': '042-333-3333'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# .items()
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기
for value in lunch.values():
    print(value)

# key 만 가져오기
for key in lunch.keys():
    print(key)