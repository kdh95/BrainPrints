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