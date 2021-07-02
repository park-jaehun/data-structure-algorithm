# coding:utf-8
graph_list = [ [],
               [2,3,8],
               [1,7],
               [1,4,5],
               [3,5],
               [3,4],
               [7],
               [2,6,8],
               [1,7]
]
visited = [False] * 9

from collections import deque
def bfs(graph, start, visited):
    # 사작 값으로 큐 초기화
    queue = deque([start])
    # 시작 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v)
        # 방문하지 않은 인접 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



print(bfs(graph_list, 1,visited))