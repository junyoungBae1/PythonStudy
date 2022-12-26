# 17219 비밀번호 찾기 https://www.acmicpc.net/problem/17219

import sys

input = sys.stdin.readline
#n 저장된 사이트 주소의 수, m 비밀번호를 찾으려는 사이트 주소의 수
n, m = map(int, input().split())

site = {}
for _ in range(n):
    a = input().split()
    site[a[0]] = a[1]

for _ in range(m):
    b = input().rstrip()
    print(site.get(b))

