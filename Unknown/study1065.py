# 1065 한수 https://www.acmicpc.net/problem/1065

def hansu(hs):
    cnt = 0
    for i in range(1, hs + 1):
        a = str(i)
        if 0 < i < 100:
            cnt += 1
        elif 100 <= i <= 1000:
            if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
                cnt += 1
    return cnt


N = int(input())
print(hansu(N))
