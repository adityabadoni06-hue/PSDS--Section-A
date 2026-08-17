class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack
stack = None

def push(data):
    global stack
    new = Node(data)
    new.next = stack
    stack = new

def pop():
    global stack
    if stack is None:
        print("Stack is empty")
    else:
        print("Popped:", stack.data)
        stack = stack.next

push(10)
push(20)
print("Stack:", stack.data, stack.next.data)
pop()

# Queue
front = rear = None

def enqueue(data):
    global front, rear
    new = Node(data)
    if rear is None:
        front = rear = new
    else:
        rear.next = new
        rear = new

def dequeue():
    global front, rear
    if front is None:
        print("Queue is empty")
    else:
        print("Dequeued:", front.data)
        front = front.next
        if front is None:
            rear = None

enqueue(10)
enqueue(20)
print("Queue:", front.data, front.next.data)
dequeue()