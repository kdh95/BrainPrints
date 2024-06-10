# 0번방부터 n-1번방까지 총 n개의 방이 있다. 0번 방을 제외한 모든 방은 잠겨있다. 우리의 목표는 모든 방에 visit하는 것이다. 하지만 잠겨저 있는 방은
# key가 없으면 visit 할 수 없다. 각 방에 방문할 때, 별개의 열쇠뭉치(a set of distict keys)를 찾을 수도 있다. 각각의 열쇠에는 number가 쓰여져 있고,
# 해당 번호에 해당하는 방을 잠금 해제할 수 있다. 열쇠뭉치는 모두 가져갈 수 있고, 언제든 방문을 열기 위해 사용할 수 있다.

# 문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
# 모든 방을 visit할 수 있다면 True, 그렇지 않으면 False를 반환하라.

# 제약조건
# n == rooms.length
# 2 <= n <= 1,000
# 0 <= rooms[i].length <= 1,000
# 1<= sum(rooms[i].length) <= 3000
# 0<= rooms[i][j] < n

# input : rooms = [[1], [2], [3], []]
# output : True

# input : rooms = [[1, 3], [3, 0, 1], [2], [0]]
# output : False


# 문제 이해하기
# n번방부터 n-1 번방까지 총 n개의 방이 있다. = 배열을 이용하면 어떨까?
# 생각을 해보면 이 문제는 무향그래프인것을 알 수 있다.
# 연결되어있는 방을 모두 방문해보면 해결책이 나오지 않을까?

# DFS/BFS 중 어떤게 더 효과적일까?
# BFS의 경우 큐가 무조건적으로 필요하다.

# DFS 의 시간복잡도는 O(Vertex + Edge)

def canVisitAllRooms(rooms):
    visited = [] # 방을 방문했는지 확인하는 리스트 선언

    # cur_v에 연결되어있는 모든 vertex에 방문할 것이다.
    def dfs(cur_v):
        visited.append(cur_v) # 방문표시를 한다.
        for next_v in rooms[cur_v]:
            if next_v not in visited: # 방문하지 않은 곳만 방문해야하기 때문에 해당 로직이 들어간다.
                dfs(next_v)

    dfs(0)

    if visited == len(rooms): return True
    else: return False

    pass


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(canVisitAllRooms(rooms))