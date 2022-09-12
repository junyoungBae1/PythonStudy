# 벌집(2292) https://www.acmicpc.net/problem/2292
# 수학
import sys
input = sys.stdin.readline

n = int(input())

d = 1 # 벌집의 개수
cnt = 1
while n > d :
    d += 6*cnt
    cnt += 1
print(cnt)

