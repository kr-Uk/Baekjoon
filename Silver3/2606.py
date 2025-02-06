"""
BFS나 DFS

예제 입력에 따른 graph값
{
    1 : [2, 5]
    2 : [3]
    3 : []
    4 : [7]
    5 : [2, 6]
    6 : []
    7 : []
}

q []
curr 1
2, 5
visited 1, 2, 5, 3, 6

"""

from collections import deque


def bfs(start, graph):
    q = deque([start])
    visited = set([start])
    
    while q:
        curr = q.popleft()
        print(curr, end=" ")
        
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                
    return visited

v = int(input())
e = int(input())
graph = {}

graph = {i: [] for i in range(1, v+1)}

for _ in range(e):
    i, value = map(int, input().split())
    graph[i].append(value)
    
print(len(bfs(1, graph))-1)
