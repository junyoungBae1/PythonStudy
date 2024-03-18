# 1080 행렬
import copy
import sys

input = sys.stdin.readline


def flip(matrix, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = 1 - matrix[i][j]


def solve(A, B, N, M):
    count = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                count += 1
    if A == B:
        return count
    else:
        return -1


N, M = map(int, input().split())
A = [list(map(int, list(input().rstrip()))) for _ in range(N)]
B = [list(map(int, list(input().rstrip()))) for _ in range(N)]

if A == B:
    print(0)
elif N < 3 or M < 3:
    print(-1)
else:
    print(solve(A, B, N, M))

#
# n, m = map(int, input().split())
#
# matrixA = [list(map(int, input().rstrip())) for _ in range(n)]
# matrixB = [list(map(int, input().rstrip())) for _ in range(n)]
# temp = copy.deepcopy(matrixA)
#
# cnt = 0


#
# def flip(arr, x, y, cnt):
#     global n, m
#     cnt += 1
#     if x + 3 == n + 1 or y + 3 == m + 1:
#         cnt = -1
#         return cnt
#
#     for k in range(x, x + 3):
#         for l in range(y, y + 3):
#             arr[k][l] = 1 - arr[k][l]
#
#     if arr == matrixB:
#         return cnt
#     elif arr != matrixB:
#         a = flip(arr, x + 1, y, cnt)
#         b = flip(arr, x, y + 1, cnt)
#         if a != -1 and b != -1:
#             return min(a, b)
#         elif a != -1:
#             return a
#         elif b != -1:
#             return b
#         else:
#             return -1
#
#
# if matrixA == matrixB:
#     print(0)
# elif n < 3 or m < 3:
#     print(-1)
# else:
#     for i in range(n - 2):
#         for j in range(m - 2):
#             cnt = 0
#             temp = copy.deepcopy(matrixA)
#             if temp == matrixB:
#                 print(cnt)
#             else:
#                 cnt = flip(temp, i, j, cnt)
#                 if cnt != -1:
#                     print(cnt)
#                     break
