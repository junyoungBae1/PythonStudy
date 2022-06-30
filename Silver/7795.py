# 7795 먹을 것인가 먹힐 것인가 https://www.acmicpc.net/problem/7795
import sys
T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    N = list(map(int, sys.stdin.readline().split()))
    M = list(map(int, sys.stdin.readline().split()))
    N.sort()
    M.sort()
    n_index = A-1
    m_index = B-1
    result = 0
    while n_index >= 0 and m_index >= 0:
        if N[n_index] > M[m_index]:
            result += m_index + 1
            n_index -= 1
        else:
            m_index -= 1

    print(result)




""" for x in N:
        left = 0
        right = B - 1 #len(M)
        mid = (left + right) // 2
        while left < right:
            print(left, right, mid, x, M[mid], result)
            if x > M[mid]:
                left = mid+1
                mid = (left + right) // 2
            elif x <= M[mid]:
                right = mid-1
                mid = (left + right) // 2
        result += mid"""