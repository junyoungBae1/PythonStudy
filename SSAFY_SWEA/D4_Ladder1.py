
T = 10
x, y = 0, 0
for tc in range(1,T+1):
    case = int(input())
    ladder = []
    for i in range(100):
        ladder.append(input().split())

    for j in range(100):
        if ladder[99][j] == '2':
            y,x = 99,j

    while y != 0:
        #좌측확인
        if 0 <= x-1 and ladder[y][x-1] == '1':
            x -= 1
            if 0 <= y - 1 and ladder[y - 1][x] == '1':
                y -= 1
        #우측확인
        elif x +1 <100 and ladder[y][x+1] =='1':
            while x+1 <100 and ladder[y][x+1] == '1':
                x += 1
            y -= 1
        #위에 확인
        elif 0 <= y - 1 and ladder[y-1][x] == '1':
            y -= 1

    print("#{} {}".format(case,x))