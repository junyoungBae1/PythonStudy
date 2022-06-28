# 4673 셀프 넘버 https://www.acmicpc.net/problem/4673

def d(p):
    s = str(p)
    self = p
    for i in s:
        self += int(i)
    return self


a = list(range(1,10001))
for i in range(1,10001):
    if d(i) in a:
        a.remove(d(i))

for i in a:
    print(i)