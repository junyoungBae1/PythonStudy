# 1806 부분합 https://www.acmicpc.net/problem/1806
# pointer?
import copy
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

#투포인터


#부분합
# cnt = 1
# result = sys.maxsize
# dp = copy.deepcopy(arr)
#
# if S < min(dp):
#     result = 0
#     print(result)
#     sys.exit(0)
# print(dp[N-1])
# for i in range(1, N):
#     dp[i-1] = arr[i-1]
#     dp[i] = arr[i]
#     for j in range(i, N):
#         if dp[j-1] < S:
#             dp[j] = dp[j - 1] + arr[j]
#             cnt += 1
#             if result < cnt:
#                 break
#         elif dp[j-1] >= S:
#             result = min(result,cnt)
#             cnt = 1
#             break
# if arr[-1] >= S:
#     print(1)
#     sys.exit(0)
# elif result == sys.maxsize:
#     print(0)
# else:
#     print(result)
# ###