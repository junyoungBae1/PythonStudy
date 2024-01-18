# 14719
# 구현

import sys

input = sys.stdin.readline

h, w = map(int, input().split())

arr = list(map(int, input().split()))

rain = 0

for i in range(1, w - 1):
    left = max(arr[:i])
    right = max(arr[i + 1:])

    compare = min(left, right)
    print("left:", left, "right:", right, "compare", compare)
    print(arr[i])
    if arr[i] < compare:
        rain += compare - arr[i]
    print("rain",rain)

print(rain)
