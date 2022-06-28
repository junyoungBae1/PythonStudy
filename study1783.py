# 1783 병든 나이트 https://www.acmicpc.net/problem/1783
N, M = map(int, input().split(" "))

# chess = [[0 for _ in range(M)] for _ in range(N)]

if N == 1:
    print(1)
elif N == 2:
    print(int(min(4, (M + 1) / 2)))
elif M < 7:
    print(min(4, M))
else:
    print(M - 2)

"""
if N == 1 or M == 1:
    print(1)
elif N == 2:
    if M == 1 or M == 2:
        print(1)
    elif M % 2 == 0:
        print(int(M / 2))
    else:
        print(int((M / 2) + 1))
else:
    if M == 1:
        print(1)
    elif M == 2:
        print(2)
    elif M == 3:
        print(3)
    elif M == 4 or M == 5:
        print(4)
    else:
        print(M - 2)
"""
"""while x < M:
    if count == 3:
        print("count 3일떄")
        if 0 < y < N:
            y += 1
            x += 2
            if x <= M+1:
                count += 1

        if 1 < y < N + 1:
            y -= 1
            x += 2
            if x <= M+1:
                count += 1

    elif N > 2:
        if 1 <= y < N - 1:
            y += 2
            x += 1
            count += 1
        elif N - 1 <= y <= N:
            y -= 2
            x += 1
            count += 1
    elif N == 2:
        if 1 <= y < N:
            y += 1
            x += 2
            count += 1
        elif y == N:
            y -= 1
            x += 2
            count += 1
    elif N == 1:
        break"""
