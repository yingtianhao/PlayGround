# coding:utf-8

a = 1
b = 2
c = 3

d = a + b + c
d += c  # 就是 d = d + c
print(d)

d -= a
print(d)

d *= b  # d = d * b
print(d)

# a /= b
# print(a)

a //= b
print(a)

c %= 2
print(c)

f = 10
f **= 2
print(f)
