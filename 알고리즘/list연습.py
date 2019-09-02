class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoFirst(data): #첫 노드에 데이터 삽입
    global Head
    Head = Node(data, Head) #새로운 노드 생성

def add(pre, data):
    if pre == None:
        print('error')
    else:
        pre.link = Node(data, pre.link)

def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)

def delete(pre):
    if pre == None or pre.link == None:
        print('error')
    else:
        pre.link = pre.link.link

def deleteFirst():
    global Head
    if pre == None:
        print('error')
    else:
        Head = Head.link

data = [1, 2, 3, 4]
Head = None

for i in range(len(data)):
    addtoFirst(data[i])

while Head.link != None:
    print(Head.data, end='->')
    Head = Head.link
print(Head.data)