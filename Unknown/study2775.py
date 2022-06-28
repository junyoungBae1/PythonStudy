#2775 부녀회장이 될테야 https://www.acmicpc.net/problem/2775

"""
모범 답안
배열 다 저장할 필요 없이 내가 필요한 곳만
num = int(input())

for i in range(num):
    floor = int(input())
    num = int(input())
    f0 = [x for x in range(1, num+1)] # 0층에 사는 사람들의 리스트
    for k in range(floor): # 층별로 쌓기
        for i in range(1, num):
            f0[i] += f0[i-1] # 해당 층의 모든 호수의 사람들의 합
    print(f0[-1])
"""

T = int(input())

for i in range(T):
    room = list()
    temp = list()
    floor = int(input()) #층
    n = int(input()) #호

    for j in range(n):
        temp.append(j+1)

    room.append(list(temp))
    temp.clear()

    for m in range(1, floor+1):

        for a in range(n):
            sum = 0
            for x in range(0, a+1):
                sum += room[m-1][x]
            temp.append(sum)

        room.append(list(temp))
        temp.clear()

    print(room[floor][n-1])
