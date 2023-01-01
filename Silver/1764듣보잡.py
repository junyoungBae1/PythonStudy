# 1764 듣보잡 https://www.acmicpc.net/problem/1764
# 교집합 &,.intersection, 합집합 |, .union, 차집합 -,.difference
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nset = set()
mset = set()
for _ in range(n):
    nset.add(input())
for _ in range(m):
    mset.add(input())

mn = sorted(list(nset & mset))
print(len(mn))

for i in mn:
    print(i)
