# 15686 치킨배달


import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = []

for i in range(n):
    row = list(map(int, input().split()))
    city.append(row)

houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

def getdistance(house,chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

min_distance_sum = 10e9

for chicken_comb in combinations(chickens, m):
    distance_sum = 0
    for house in houses:
        distance_sum += min(getdistance(house,chicken) for chicken in chicken_comb)
    min_distance_sum = min(min_distance_sum,distance_sum)

print(min_distance_sum)