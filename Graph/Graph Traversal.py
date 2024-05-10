# 그래프 순회
# 그래프 순회란 그래프 탐색(search)라고도 불리우며, 그래프의 각 정점을 방문하는 과정을 말한다.
# 그래프 순회에는 크게 깊이 우선 탐색(Depth-First Search)과 너비 우선 탐색(Breadth-First Search)의 2가지 알고리즘이 있다.



# 1. 너비 우선 탐색(BFS)
graph = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

# 이걸 외우자 가장 기본적인 템플릿이다.
from collections import deque

def bfs(graph, start_v):
    visited = [start_v] # 배열 초기화
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

bfs(graph, 'A')
# return 되는 visited가 그래프를 bfs로 순회한 순서이다.





# 2. 깊이 우선 탐색 (DFS)

