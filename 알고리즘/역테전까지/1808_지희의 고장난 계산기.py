import sys
sys.stdin = open('1808_input.txt')

def find():

    for i in range



T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = int(input())
    num = []

    for i in range(len(arr)):
        if arr[i]:
            num.append(i)