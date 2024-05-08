
from collections import deque


def maxDepth(root):
    max_depth = 0
    if root is None:
        return max_depth
    q = deque()
    q.append(root, 1) # depth 정보도 함께 넘겨준다.
    while q:
        cur_node, cur_depth = q.popleft()
        max_depth = max(max_depth, cur_depth) # 둘 중 큰 값으로 depth 값 설정
        if cur_node.left:
            q.append(cur_node.left, cur_depth + 1)
        if cur_node.right:
            q.append(cur_node.right, cur_depth + 1)

    return max_depth



root = [3, 9, 20, None, None, 15, 7]

class TreeNode:
    def _init_(self, l=None, r=None, v=0): # 초기화시 left, right 노드에 값이 없으면 None으로 초기화, value 값이 없으면 0으로 초기화
        self.left = l
        self.right = r
        self.value = v


root = TreeNode(v=3) # root node 초기화
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))