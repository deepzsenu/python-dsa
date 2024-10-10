def push(data):
    # Your code here
    global stack
    global stackMax
    global top
    top += 1
    if top > 100000:
        print("Stack Full")

    else:
        stack[top] = data


def pop():
    # Your code here
    global stack
    global top
    global stackMax
    if top <= -1:
        print("Stack Empty")
    else:
        stack[top] = stack[top-1]
        top = top - 1


def display():
    # Your code here
    global stack
    global top
    global stackMax
    if top <= -1:
        print('-1')
    else:
        i = 0
        while i <= top:
            print(stack[i], end=" ")
            i = i + 1
        print()


def rev(q):

    Stack = []
    while (not q.empty()):
        Stack.append(q.queue[0])
        q.get()
    while (len(Stack) != 0):
        q.put(Stack[-1])
        Stack.pop()
    return q
