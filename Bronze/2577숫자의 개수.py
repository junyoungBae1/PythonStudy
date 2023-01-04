a = int(input())
b = int(input())
c = int(input())
d = a * b * c
e = str(d)
count = 0
for i in range(0,10):
    for j in e:
        if j == str(i):
            count += 1
    print(count)
    count = 0
