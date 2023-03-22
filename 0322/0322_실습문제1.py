from vpython import *
a = vec(1, 2, 3)
b = vec(0, 2, 4)

# 1번 문제
print('inner product:', dot(a, b))

# 2번 문제
r = vec(2, -2, 2)
print('magnitude:', mag(r))
print('norm:', norm(r))

# 3번 문제
v = vec(3, 4, 0)
v_arrow = arrow(pos=vec(0, 0, 0), axis=v, color=color.white, shaftwidth=0.2)
e1 = vec(1, 0, 0)
b = dot(v, e1)*e1
b_arrow = arrow(pos=vec(0, 0, 0), axis=b,
                color=color.blue, shaftwidth=0.1)
a_arrow = arrow(pos=vec(0, 0, 0), axis=v-b,
                color=color.red, shaftwidth=0.1)
print('parallel:', b)
print('perpendicular:', v-b)
