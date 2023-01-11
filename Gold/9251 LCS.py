# 9251 LCS(최장 공통 부분 수열) https://www.acmicpc.net/problem/9251

import sys
from itertools import combinations

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
s1 = len(str1)
s2 = len(str2)
matrix = [[0] * (s2+1) for _ in range(s1+1)]

for i in range(1, s1+1):
    for j in range(1, s2+1):
        if str1[i - 1] == str2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])

print(matrix[-1][-1])

"""
def LCS(cnt):
    result = 0
    for i in range(1, cnt):
        for word1 in combinations(str1, i):
            for word2 in combinations(str2, i):
                if word1 == word2:
                    if result < i:
                        result = i
        if result < i:
            return result


print(LCS(cnt))
"""
