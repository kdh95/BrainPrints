
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
