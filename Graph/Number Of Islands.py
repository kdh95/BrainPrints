# grid는 "1"(land) 과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원배열이다.
# 이 지도에 표시된 섬들의 총 갯수를 반환하시오.
# 섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러쌓여 있는 것을 말한다.
# 또한, grid의 네개의 가장자리는 모두 물로 둘러쌓여있다고 가정하고 문제를 해결하라.

# 제약조건
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'

# input : grid = [
#               ['1', '1', '1', '1', '0'],
#               ['1', '1', '0', '1', '0'],
#               ['1', '1', '0', '0', '0'],
#               ['0', '0', '0', '0', '0']
#          ]

# output : 1


# input : grid = [
#               ['1', '1', '0', '0', '0'],
#               ['1', '1', '0', '0', '0'],
#               ['0', '0', '1', '0', '0'],
#               ['0', '0', '0', '1', '1']
#          ]

# output : 3


# 해당 문제는 그래프 문제이다.
# bfs? or dfs?
# 이차원 배열로 무언가를 표현한다 -> 그래프문제일 가능성이 높다.
# bfs or dfs를 사용하면 모두 방문이 가능할거 같다.
# 그럼 섬의 개수를 어떻게 count 할 수 있을까?
# 1이 연결된 애들을 색칠하면 어떨까? 방문을 하면서

# 내가봤을땐 bfs로 하는게 더 직관적인것 같다. 주변에 1이 있는지 찾아가면서 색칠을 하는 것이다.


# 1. BFS로 문제 해결하기
# 이중 for문을 돌면서 BFS를 하면 될 것 같다.

from collections import deque  # 큐 자료구조를 사용할것이다.


def numIslands(grid):
    number_of_islands = 0  # 마지막에 리턴해줄 섬의 개수 변수
    m = len(grid)  # 그리드의 가로줄의 개수
    n = len(grid[0])  # 그리드의 세로줄의 개수
    visited = [[False] * n for _ in range(m)]  # 방문했는지 알 수 있는 변수 = 색칠

    # 함수를 함수안에 넣은 이유 밖에 있게 되면 재귀호출될때 변수를 넘기게 되면 메모리게 누적해서 변수가 선언되기 떄문에 그것을 방지하기 위해
    def bfs(x, y):
        dx = [-1, 1, 0, 0]  # 상,하,좌,우 순서로 이동하고 싶을때 이렇게 선언한다.
        dy = [0, 0, -1, 1]
        visited[x][y] = True  # 방문을 했다고 표시한다.
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            # 상,하,좌,우를 모두 방문하고 싶다면 이렇게 한다. 대각선은 뒤에 더 추가해주면 된다.
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                # 범위를 넘어가는지 체크
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    # "1" 섬이고, 방문한적이 없는 경우에 로직 수행
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                number_of_islands += 1
    return number_of_islands


print(numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
