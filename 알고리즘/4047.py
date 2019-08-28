import sys
sys.stdin = open('4047_input.txt')

T = int(input())

for tc in range(1, T+1):

    # 한덱 : 스페이드, 다이아몬드, 하트, 클로버 (S, D, H, C)
    # 각각 A, 2~10, K, Q, K 로 총 13장의 카드가 있다.
    # 몇장의 카드가 부족한지 찾는 문제

    # 3자리씩 한 카드의 정보이므로 리스트로 묶어서 나눠주기
    # 겹치는게 있으면 error
    # 각 타드별로 카운팅에서 있는 개수를 빼준다.

    now = [[] for _ in range(4)] # 0: S, 1: D, 3: H, 4: C
    arr = input()
    tmp = ''

    for i in range(0, len(arr), 3):
        card = '{}{}{}'.format(arr[i], arr[i+1], arr[i+2])
        if arr[i] == 'S' and card not in now[0]:
            now[0].append(card)
        elif arr[i] == 'D' and card not in now[1]:
            now[1].append(card)
        elif arr[i] == 'H' and card not in now[2]:
            now[2].append(card)
        elif arr[i] == 'C' and card not in now[3]:
            now[3].append(card)
        else:
            tmp = 'ERROR'

    cnt = [0] * 4

    for i in range(4):
        cnt[i] = 13 - len(now[i])

    if tmp != 'ERROR':
        print('#{} {}'.format(tc, ' '.join(list(map(str, cnt)))))
    else:
        print('#{} {}'.format(tc, tmp))




