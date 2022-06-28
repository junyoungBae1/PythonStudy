# 13305 주유소 https://www.acmicpc.net/problem/13305
# O(N) 이여야함 // O(N^2)이면 안됨
N = int(input())
r = input().split(" ")
cost = input().split(" ")
result = 0

for i in range(N - 1):
    if int(cost[i]) < int(cost[i + 1]):
        cost[i + 1] = cost[i]
for i in range(N - 1):
    result += int(cost[i]) * int(r[i])

print(result)

