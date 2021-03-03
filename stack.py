class Node:

    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.key) 

class Stack:

    def __init__(self):
        self.head = None

    def push(self, x):
        node = Node(x)
        if self.head != None:
            self.head.prev = node
            node.next = self.head
        self.head = node
        print(self.head)

    def pop(self):
        if self.head == None:
            raise Exception('Empty Stack')
        node = self.head
        if node.next != None:
            node.next.prev = None
        self.head = node.next
        return node

    def __str__(self):
        s = ''
        node = self.head
        while node != None:
            s = str(node.key) + ' ' + s
            node = node.next
        return s

s = Stack()
s.push(3)
print(s)
s.push(4)
print(s)
s.push(5)
print(s)
s.push(6)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
s.push(2)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
s.pop()
