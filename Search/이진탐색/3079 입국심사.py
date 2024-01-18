#3079 입국심사https://baebalja.tistory.com/362

#이분탐색

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
k = []
for i in range(n):
    x = int(input().strip())
    k.append(x)

low = 0
high = max(k)*m
result = high

while low <= high:
    total = 0
    mid = (low+high) // 2

    for i in k:
        total += mid//i

    if total >= mid:
        high = mid -1
        print(result)
        result = min(mid,result)
    else:
        low = mid + 1

print(result)

# 떙



