# 15654 N과M(5) https://www.acmicpc.net/problem/15654

# import sys
# from itertools import permutations
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# per = list(permutations(arr,M))
#
# per = sorted(per)
#
# for i in per:
#     for j in i:
#         print(j, end=' ')
#     print("")
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
visited = [0] * N
out = []

def dfs():
    if len(out) == M:
        print(' '.join(map(str, out)))
        return

    for i in range(N):
        if not visited[i]:
            out.append(arr[i])
            visited[i] = True
            dfs()
            visited[i] = False
            out.pop()

dfs()

