from collections import deque
stack=deque([1,2,3,4])
print(stack)
stack.appendleft(5)
print(stack)
stack.popleft()
print(stack)
