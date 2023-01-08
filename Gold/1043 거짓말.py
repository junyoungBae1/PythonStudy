# 1043 거짓말  https://www.acmicpc.net/problem/1043
#Union-Find 그래프 알고리즘, 합집합 찾기
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
know = set(input().split()[1:])
cnt = 0
p = []

for i in range(m):
    p.append(set(input().split()[1:]))


for _ in range(m):
    for party in p:
        if party & know:
            know = know.union(party)

for party in p:
    if party & know:
        continue
    cnt += 1

print(cnt)
