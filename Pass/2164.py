from collections import deque

n = int(input())
q = deque([i for i in range(1, n+1)])

while len(q) != 1:
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)
    
print(q.pop())