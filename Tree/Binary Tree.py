from collections import deque

class Node:
    def _init_(self, value = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def _init_(self):
        self.root = None


bt = BinaryTree()
bt.root = Node(value = 1)
bt.root.left = Node(value = 2)
bt.root.right = Node(value = 3)
bt.root.left.left = Node(value = 4)




## 트리 순회 (Tree Traversal)
## 트리슨회란 트리탐색이라고도 불리우며, 트리의 각 노드를 방문하는 과정을 말한다.
## 모든 노드를 한 번씩 방문해야 하므로 완전 탐색이라고도 불린다. 순회 방법으로는
## 너비 우선 탐색의 BFS와 깊이 우선 탐색의 DFS가 있다.

# BFS (가장 기본 외우자)
def bfs(root):
    visited = [] # 트리에 접근했던 이력을 남긴다.
    if root is None: # root가 없으면 빈 트리이다.
        return 0; # or []
    q = deque() # deque 자료구조를 사용한다. bfs를 하려면 deque 자료구조를 사용한다.
    q.append(root) # root 노드를 deque에 넣는다. 여기까지가 초기셋팅
    while q: # deque가 비워질때까지 반복문을 돈다.
        cur_node = q.popleft() # 노드에 접근하는 부분  ex)root 노드에 접근한것이다.
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left) # left child 노드가 있으면 해당 노드의 주소값을 방문리스트에 담는다.
        if cur_node.right:
            q.append(cur_node.right) # right child 노드가 있으면 해당 노드의 주소값을 방문리스트에 담는다.
    return visited


bfs(bt)



# DFS (깊이 우선 탐색)
# 1. Stack 반복문과 2. 재귀(recursion)이 존재하는데
# 2. 재귀를 사용할 것이다.

# 접근 방법에 대한 로직
def dfs(cur_node):
    if cur_node is None: # 이 부분이 처음 root 노드로 돌아왔을떄 return 하는 부분이다.
        return
    dfs(cur_node.left)
    dfs(cur_node.right)

dfs(bt) # root 노드만 제공하면 root가 가리키는 Tree에 속한 모든 노드에 접근가능하다.

# 재귀를 사용하는 방법은 각 노드는 서브트리라는 개념을 사용한 것이다.

