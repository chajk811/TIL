## 1
import sys
sys.stdin = open('Flatten_input.txt')

for case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    while dump > 0:
        MAX, MIN = boxes[0], boxes[0]
        idx_max, idx_min = 0, 0

        for idx, val in enumerate(boxes):
            if MAX < val:
                MAX = val
                idx_max = idx
            if MIN > val:
                MIN = val
                idx_min = idx

        boxes[idx_max] = MAX - 1
        boxes[idx_min] = MIN + 1

        dump -= 1

    result = max(boxes) - min(boxes)
    print('#{} {}'.format(case, result))


## 2
# import sys
# sys.stdin = open('Flatten_input.txt')
#
#     for test_case in range(1, 11):
#         dump = int(input())
#         arr = list(map(int, input().split()))
#         cnt = [0] * 101
#         for val in arr:
#             cnt[val] += 1
#         minIdx, maxIdx = 0, 100
#         i = 0
#         while i < dump:
#             while cnt[minIdx] == 0: minIdx += 1
#             while cnt[maxIdx] == 0: maxIdx -= 1
#             cnt[minIdx] -= 1
#             cnt[minIdx + 1] += 1
#             cnt[maxIdx] -= 1
#             cnt[maxIdx - 1] += 1
#             i += 1
#         if cnt[minIdx] == 0: minIdx += 1
#         if cnt[maxIdx] == 0: maxIdx -= 1
#         print("#%d %d" % (test_case, maxIdx - minIdx))