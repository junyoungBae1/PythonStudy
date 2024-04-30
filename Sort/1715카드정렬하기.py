import sys
import heapq

input = sys.stdin.readline

n = int(input())
card = []
result = 0
for i in range(n):
    heapq.heappush(card,int(input()))

while len(card) >= 2:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    new_bundle = a + b
    result += new_bundle
    heapq.heappush(card,new_bundle)

print(result)