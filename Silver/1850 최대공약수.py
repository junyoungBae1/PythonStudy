# 1850 최대공약수


a, b = map(int, input().split())


# # z = max(na, nb)
# arr = [1 for _ in range(z)]
# a = ""
# b = ""
# for i in range(z):
#     a += str(arr[i])

#
# for i in range(nb):
#     b += str(arr[i])
#
# a = int(a)
# b = int(b)
#

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


print("1" * gcd(a, b))
