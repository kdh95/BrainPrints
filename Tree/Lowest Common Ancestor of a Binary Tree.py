# Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다
# 이 때, 두 노드의 공통 조상중 가장 낮은 node 즉, the lowest common ancestor(LCA)를 찾아라.

# 제약조건
# 2<= node 개수 <= 10^5
# -10^9 <= Node.val <= 10^9
# 모든 Node.val은 Unique하다.
# p != q
# p,q는 모두 주어진 Tree에 속해 있다.


# ex) input : root, p = 5, q = 1
# ex) ouput : 3



# 재귀함수라는 것을 잊으면 안된다.

# left child와 right child 정보를 알아야 return 값을 정할 수 있기 때문에
# 후위순위 방법으로 풀어야한다.
def LCA(root, p, q):
    if root == None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right


LCA([3,5,1,6,2,0,8,None,None,7,4], 6, 4)