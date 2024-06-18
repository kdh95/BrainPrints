# Climbing stairs

# 계단을 올라가고 있다. 이 계단의 꼭대기에 도착하려면 n개의 step만큼 올라가야 한다. 한 번 올라갈 때마다
# 1 step 또는 2 steps 올라갈 수 있다. 꼭대기에 도달하는 방법의 개수는 총 몇가지 일까요?

# 제약조건
# 1 <= n <= 45

# input : n = 2
# output : 2
# 1. 1 step + 1 step
# 2. 2 steps


# input : n = 3
# output : 3
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# 접근방법 => 완전탐색
# 1. 크고 복잡한 문제를 하위 문제로 나눈다.
# 2. 하위 문제에 대한 답을 계산한다.
# 3. 하위 문제에 대한 답으로 원래 문제에 대한 답을 계산한다.

# 5층으로 갈 수 있는 경우의 수는 몇가지 인가?
# 4층에서 올라가거나 3층에서 올라가는 경우의 수 2가지 밖에 없다.
# 따라서 3층까지 올라가는 경우의 수와 4층까지 올라가는 경우의 수를 모두 더하면 되지 않을까?
# 피보나치 수열과 똑같다.


# def cs(n):
#     if n == 1:
#         return 1 # 1층을 올라가는 경우의 수
#     if n == 2:
#         return 2 # 2층을 올라가는 경우의 수
#
#     return cs(n-1) + cs(n-2)


# TOP-DOWN 방식 => 재귀를 사용한다.
memo = {}

def cs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo:
        memo[n] = cs(n-1) + cs(n-2)
    return memo[n]


# BOTTOM-UP 방식 => 반복문을 사용한다.
# basecase 2층 : 2, 1층 : 1
memo = {1: 1, 2: 2}

def cs(n):

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]



