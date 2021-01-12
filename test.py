from collections import deque

if __name__ == '__main__':
    s = "Data/driven/tech"

    stack = deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack)
    stack.popleft()
    print(stack)
