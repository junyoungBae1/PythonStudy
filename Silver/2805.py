# 2805 나무 자르기 https://www.acmicpc.net/problem/2805
# 이분탐색

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
left = 0
right = max(tree)-1

while left <= right:
    sum = 0
    mid = (right + left) // 2
    for i in tree:
        if i > mid:
            sum += i - mid
        if sum > m:
            break
    if sum < m:
        right = mid-1
    elif sum >= m:
        left = mid+1

print(right)