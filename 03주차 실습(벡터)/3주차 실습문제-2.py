from vpython import *

# 1번 문제
x = 0
u = vec(1, 2, 3)
v = vec(7, -2, x)

x = (7+(-4))/(-3)
v = vec(7, -2, x)

print('inner product:', dot(u, v))


# 2번 문제
a = vec(1, 2, 3)
b = vec(2, -1, 1)
c = cross(a, b)
d = cross(b, a)

a_arrow = arrow(pos=vec(0, 0, 0), axis=a, color=color.red)
b_arrow = arrow(pos=vec(0, 0, 0), axis=b, color=color.blue)
c_arrow = arrow(pos=vec(0, 0, 0), axis=c, color=color.green)
d_arrow = arrow(pos=vec(0, 0, 0), axis=d, color=color.purple)

print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
