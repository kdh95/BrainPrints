# 계단을 올라가고 있다. 한 번 올라갈 때마다 1 step 또는 2 step 올라갈 수 있다.
# 문제에서 정수형 배열 cost가 주어지는데, cost[i]는 i번째 계단을 밟았을 때 지불해야 하는 비용이다.
#
# 처음 시작은 index 0  또는 index 1 중 한 곳에서 시작할 수 있다.한
#
# 이 계단의 꼭대기에 도착하기 위해 지불해야하는 비용의 최소값을 반환하라.
# (return the minimum cost to reach the top of the floor)
#
# 제약조건
# 2 <= cost.length <= 1000
# 0 <= cost.[i] <= 999
#
# input : cost = [10, 15, 20]
# output : 15
#
# input : cost = [1,100,1,1,1,100,1,1,100,1]
# output : 6


# 완전탐색으로 모두 확인해보면 되지 않을까?
# O(N^2) 으로 풀면 되겠다.