#1215

T = 10

for tc in range(1,T+1):
    result = 0
    resultlist = []
    n = int(input())
    arr = []
    a = input()
    lens = len(a)
    arr.append(a)
    for _ in range(lens-1):
        x = input()
        arr.append(x)

    for i in range(lens):

        for j in range(lens-n+1):
            left = j
            right = n - 1 + j
            while 1:
                if left == right or left > right:

                    resultlist.append(arr[i][j:n+j])
                    break

                if arr[i][left] == arr[i][right]:
                    left += 1
                    right -= 1
                else:
                    break

    for i in range(lens):
        for j in range(lens - n + 1):
            left = j
            right = n - 1 + j
            while 1:
                if left == right or left > right:
                    vertical_str = ''.join(arr[k][i] for k in range(j, j + n))

                    resultlist.append(vertical_str)
                    break
                if arr[left][i] == arr[right][i]:
                    left += 1
                    right -= 1
                else:
                    break

    result = len(resultlist)
    print("#{} {}".format(tc,result))

'''
T = 10

for tc in range(1,T+1):
    result = 0
    n = int(input())
    arr = [input() for _ in range(8)]

    for i in range(8):
        for j in range(8-n+1):
            # 가로 방향 검사
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                result += 1

            # 세로 방향 검사
            vertical_str = ''.join([arr[k][i] for k in range(j, j+n)])
            if vertical_str == vertical_str[::-1]:
                result += 1

    print("#{} {}".format(tc,result))
'''