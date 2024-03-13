# 2529 부등호


import sys

input = sys.stdin.readline

n = int(input())
sign = [""] + input().rstrip().split()
temp = []
ans = []

def solve(idx):
    if idx == n + 1:
        _num = ''.join(map(str, temp))
        ans.append(_num)
        return

    for i in range(10):
        if not i in temp:
            if idx == 0 or (sign[idx] == ">" and temp[-1] > i) or (sign[idx] == "<" and temp[-1] < i):
                temp.append(i)
                solve(idx + 1)
                temp.pop()

solve(0)

print(ans[-1])
print(ans[0])
