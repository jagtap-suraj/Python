queue = []

def isEmpty():
    return (queue == [])

def display():
    if isEmpty() == 0:
        return queue
    else:
        return -1

def queueSize():
    return len(queue)

def enque(element):
    queue.append(element)

def peek():
    if isEmpty() == 0:
        return queue[len(queue) - 1]
    else:
        return -1

def deque():
    if isEmpty() == 0:
        return stack[0]
    else:
        return -1
