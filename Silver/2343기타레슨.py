#2343기타레슨

import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
answer = 0
start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    count,sum = 0,0

    for i in range(n):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]
    if sum:
        count += 1

    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)