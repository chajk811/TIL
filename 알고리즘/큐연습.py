# 튜 동작 구현
# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고
# 튜에서 세개의 데이터를 차례로 꺼내서 출력한다. (ex. 1 2 3)

Q = []

for i in range(1, 4):
    Q.append(i)

for i in range(3):
    a = Q.pop(0)
    print(a, end=' ')


# import queue
# q=queue.Queue()
# q.put('A')
# q.put('B')
# q.put('C')
#
# while not q.empty():
#     print(q.get())
