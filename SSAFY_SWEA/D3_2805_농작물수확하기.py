# 2805

T = int(input())

for tc in range(1, T + 1):
    sum = 0
    n = int(input())

    arr = [input() for _ in range(n)]

    if n == 1:
        print("#{} {}".format(tc, arr[0][0]))
    else:
        mid = n // 2
        right = mid
        left = mid
        for i in range(mid):
            if left == right:
                sum += int(arr[i][mid])
                right += 1
                left -= 1
            else:
                for j in range(left, right + 1):
                    sum += int(arr[i][j])
                right += 1
                left -= 1

        for i in range(mid, n):
            if left == right:
                sum += int(arr[i][mid])
                right -= 1
                left += 1
            else:
                for j in range(left, right + 1):
                    sum += int(arr[i][j])
                right -= 1
                left += 1

        print("#{} {}".format(tc, sum))
