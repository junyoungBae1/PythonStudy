# 1072 게임 https://www.acmicpc.net/problem/1072
# 이분 탐색 , 소수점 계산

X, Y = map(int, input().split())
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
            left = mid + 1
        else:
            result = mid
            right = mid - 1

    print(result)


""" 시간초과... O(N)의 방법이었다..

X, Y = map(int, input().split())

Z = str(Y * 100 // X)
count = 0
flag = 1
if Z[0] == '9' and Z[1] == '9':
    count -= 1
else:
    if X > 10000:

        while flag:
            temp = str((Y + 10000) * 100 // (X + 10000))
            print(temp)
            if X == Y:
                count -= 1
                break
            if Z[0] == "0" and Z[0] == temp[0]:
                X += 10000
                Y += 10000
                count += 10000
            elif Z[0] != "0" and Z[1] == temp[1]:
                X += 10000
                Y += 10000
                count += 10000
            else:
                count += 10000
                flag = 0
    flag = 1
    while flag:
        temp = str((Y+1)*100 / (X+1))
        print(temp)
        if X == Y:
            count -= 1
            break
        if Z[0] == "0" and Z[0] == temp[0]:
            X += 1
            Y += 1
            count += 1
        elif Z[0] != "0" and Z[1] == temp[1]:
            X += 1
            Y += 1
            count += 1
        else:
            count += 1
            flag = 0


print(count)"""
