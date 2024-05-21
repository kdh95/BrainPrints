# n x n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지 까지 도착하는 가장 빠른 경로의 길이를 반환하시오.
# 만약 경로가 없다면 -1을 반환하시오

# 출발지 : top-left cell
# 목적지 : bottom - right cell

# - 값이 0인 cell만 지나갈 수 있다.
# cell끼리는 8가지 방향으로 연결되어 있다. (edge와 corner 방향으로 총 8가지 이다.)
# 연결된 cell을 통해서만 지나갈 수 있다.

# 제약조건
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

# input : grid = [
#               [0, 0, 0],
#               [1, 1, 0],
#               [1, 1, 0]
#         ]

# output : 4


# input : grid = [
#               [1, 0, 0],
#               [1, 1, 0],
#               [1, 1, 0]
#         ]

# output : -1

# 문제 이해하기
# 8가지 방향으로 연결되어 있다는 것이 중요하다. (=대각선으로 이동 가능)
# 출발지가 1이면 무조건 -1이겠다. 목적지가 1이면 어떻게 될까? 무조건 -1이 될 것이다.
# 제약조건에서 n >=1 인데 cell 이 한개면 어떻게 될까?
# 모든 vertex를 한번씩 방문하여 최단거리를 구하려면 BFS를 사용하면 된다.
# 시간 복잡도는 vertex의 갯수만큼 걸리게 된다.
# 제약조건에서 10^2까지 n의 개수를 정해두었기 때문에 BFS로 풀 수 있는 근거가 된다.
# 만약 DFS로 풀게되면 모든 경우의 수를 다 따져봐야 최단거리인지 알 수 있다.


# 무조건 queue를 사용할 것이기 떄문에 먼저 import 해준다.
from collections import deque

def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])

    if grid[0][0] != 0:
        return shortest_path_len

    visited = [[False] * col for _ in range(row)]

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True # 예약을 했기 때문에 바로 바꿔준다.

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        # 목적지에 도착했을 때 그때의 cur_len를 shortest_path_len에 저장하면 된다.
        if cur_r == row - 1 and cur_c == col - 1:
            shortest_path_len = cur_len
            break

        # 연결되어있는 모든 vertex 확인하기
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True


    return shortest_path_len



