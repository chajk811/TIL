'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
if number % 2 == 0:
    print(f'입력 받은 숫자 {number}은(는) 짝수입니다.')
else:
    print(f'입력 받은 숫자 {number}은(는) 홀수입니다.')

#답
if number % 2:
    print('홀수입니다.')
else:
    print('짝수입니다.')