import sys
sys.stdin = open('2117_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]

    # 5 <= N <= 20
    # 1 <= M <= 10
    # 운영 비용 = K * K + (K-1) * (K-1)
    # 이익 = (서비스 제공받는 집 * M) - 운영비용
    # 손해를 보지 않고 서비스 가능한 최대 집의 수
