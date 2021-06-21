# -*- coding: euc-kr -*-
from collections import deque
# BFS �Լ� ����
def bfs(graph, start, visited):
    #ť ������ ���� deque ���̺귯�� ���
    queue = deque([start])
    visited[start] = True
    # ���� ��带 �湮 ó��
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]


visited = [False] * 9
bfs(graph, 1, visited)
print("")
visited = [False] * 9
dfs(graph, 1, visited)