from vpython import *

ground = triangle(v0=vertex(pos=vec(0, 0, 0)),
                  v1=vertex(pos=vec(8, 0, 0)),
                  v2=vertex(pos=vec(0, 6, 0)))

o = vec(0, 0, 0)
a = vec(8, 0, 0)
b = vec(0, 6, 0)
theta = diff_angle(a, a-b)

ball = sphere(pos=vec(0, 6, 0), radius=0.1)
ball.m = 1
ball.v = vec(0, 0, 0)

ball.f = vec(0, 0, 0)

t = 0
dt = 0.001

g = vec(0, -9.8, 0)

while(ball.pos.y >= 0):
    rate(1/dt)

    ball.f = (ball.m*sin(theta)*mag(g))*(norm(a-b))

    ball.v += (ball.f/ball.m)*dt
    ball.pos += (ball.v)*dt

    t += dt

print('coding :', t)
print('theory :', sqrt(2*(3/5)*10*(25/9)*(1/mag(g))))
