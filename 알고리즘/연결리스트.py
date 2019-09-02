class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link


def push(i):
    global top
    top = Node(i, top)

def pop():
    global top
    if top == None:
        print('error')
    else:
        data = top.data
        top = top.link
        return data

top = None
push(3)
push(4)
push(5)
push(6)
pop()

while top.link != None:
    print(top.data, end='=>')
    top = top.link
print(top.data)