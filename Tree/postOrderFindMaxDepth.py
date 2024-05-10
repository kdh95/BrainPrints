# post order 방법으로 maxDepth (깊이) 찾기
# 모든 노드를 방문하는데 levelorder 와 다르게 깊이를 우선으로 노드 탐색을 한다.
# 자식노드에서 리턴해준 값을 비교하여 깊이를 확인한다.


# 트리 만들기
class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3) # 왼쪽 노드트리
root.left = TreeNode(v=5)
root.left.left = TreeNode(v=6)
root.left.right = TreeNode(v=2)
root.left.right.left = TreeNode(v=7)
root.left.right.right = TreeNode(v=4)

root.right = TreeNode(v=1) # 오른쪽 노드트리
root.right.left = TreeNode(v=0)
root.right.right = TreeNode(v=8)



def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1 # 둘 중에 큰 값에 +1 해줘야 한다.


print(maxDepth(root))