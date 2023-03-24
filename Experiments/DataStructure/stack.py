stack = []

def isEmpty():
    return (stack == [])

def display():
    if isEmpty() == 0:
        return stack
    else:
        return -1

def stackSize():
    return len(stack)

def push(element):
    stack.append(element)

def peek():
    if isEmpty() == 0:
        return stack[len(stack) - 1]
    else:
        return -1

def pop():
    if isEmpty() == 0:
        return stack.pop()
    else:
        return -1
