# 1244


for tc in range(1,int(input())+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])

    nxt = set()
    for _ in range(K):

        while now:
            print(now)
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    print("s",s,"nxt",nxt)
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc,max(map(int,now))))