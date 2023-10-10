T = 10
for test_case in range(1, T + 1):
    N = int(input())
    build = list(map(int, input().split()))
    result = 0
    for i in range(2, N - 2):
        side = max(build[i - 2], build[i - 1], build[i + 1], build[i + 2])
        if build[i] > side:
            result = result + build[i] - side
    print("#{} {}".format(test_case, result))
