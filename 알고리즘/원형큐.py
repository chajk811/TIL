def isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(cQ) == front

def enQueue(item): # 원형 큐의 삽입 연산
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item

def deQueue(): # 원형 큐의 삭제 연산
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]

cQ_SIZE = 3
cQ = [0] * cQ_SIZE

front = rear = 0 # front와 rear를 0으로 초기화

enQueue('a')
enQueue('b')
enQueue('c')
print(deQueue())
print(deQueue())
print(deQueue())