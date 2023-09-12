# 1072 게임 https://www.acmicpc.net/problem/1072
# 이분 탐색 , 소수점 계산

X,Y = map(int,input().split())
Z = (Y * 100) // X
if Z >= 99:
    print(-1)
else:
    result = 0
    left = 1
    right = X

    while left <= right:
        mid = (left + right) // 2
        if (Y+mid) * 100 // (X+mid) <= Z:
            left = mid+1
        else:
            result = mid
            right = mid-1
    print(result)

