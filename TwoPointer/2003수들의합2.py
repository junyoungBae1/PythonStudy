#2003 수들의 합2 https://www.acmicpc.net/problem/2003

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
end = 0
dp = 0
#start를 증가시키며 반복
for start in range(N):
    #end만큼 이동
    while dp < M and end <N:
        dp += arr[end]
        end +=1
    # 부분합이 dp
    if dp == M:
        result +=1
    dp -= arr[start]

print(result)