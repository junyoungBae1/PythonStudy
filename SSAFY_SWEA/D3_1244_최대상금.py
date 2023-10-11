# 1244


T = int(input())
for test_case in range(1, T + 1):
    answer = -1
    value, cnt = input().split()
    n = len(value)
    cnt = int(cnt)
    now = {value}
    nxt = set()
    for _ in range(n):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(n):
                for j in range(i + 1, n):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now
    answer = max(map(int, now))
    print("#{} {}".format(test_case, answer))

for tc in range(1,int(input())+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc,max(map(int,now))))