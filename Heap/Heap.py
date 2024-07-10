# Heap
# 완전 이진 트리 (complete binary tree) 형태의 자료구조이다.

# 완전 이진 트리의 특성
# 완전 이진 트리의 경우 배열로 표현이 가능하다. 부모의 인덱스 = (i-1)/2, 자식 인덱스 = 2^i-1

# min heap : 부모 노드의 값이 자식 노도의 값보다 작은 트리 형태의 자료구조
# max heap : 부모 노드의 값이 자식 노드의 값보다 큰 트리 형태의 자료구조

# 형 노드 간에는 대소 관계가 정해지지 않는다.
# Root 노드가 가장 큰(or 작은) 값을 갖는다.


# 구현 - Heap
import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]
print(min_heap)
heapq.heapify(min_heap) # 부모 노드의 값이 자식 노드의 값보다 작다.
print(min_heap)

# heap pop
# dequeue
heapq.heappop(min_heap) # -> dequeue 우선순위가 가장 높은 root 노드가 사라진다.
# 그리고 맨 마지막에 있는 노드를 root 노드로 가져온다.
# 그러면 정의에 어긋나게된다.
# 그렇기 때문에 우선순위를 바로잡게 된다. 자식노드들 중 가장 작은 값을 비교해서 우선순위가 높은 노드로 root로 가져온다.
# 위 방법을 반복해서 다시 완전 이진 트리를 만들게 된다.
# 이 방법을 shift down 이라고 하는데 트리의 높이 만큼 실행하게 된다. 시간복잡도 = O(logN)
print(min_heap)


# heap push
# enqueue
heapq.heappush(min_heap, 1)
# 이번에는 shift up을 진행한다. 부모 노드와 값을 비교해서 스왑을 진행한다.
# 위 방법을 반복한다. 트리의 높이만큼 반복하기 때문에 시간복잡도는 O(logN)이 된다.
