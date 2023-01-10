# 15686 치킨 배달 https://www.acmicpc.net/problem/15686

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

city = []
house = []
chicken = []
result = 1e6

for i in range(n):
    row = list(map(int, input().split()))
    city.append(row)
    for j in range(n):
        if row[j] == 1:
            house.append((i,j))
        elif row[j] == 2:
            chicken.append((i,j))


for i in combinations(chicken,m):
    total_distance = 0
    for r1,c1 in house:
        distance = 1e6
        for r2,c2 in i:
            distance = min(distance, abs(r1-r2)+abs(c1-c2))
        total_distance += distance
    result = min(result, total_distance)

print(result)