from vpython import *

x_axis = arrow(pos=vec(0,0,0), axis=vec(15,0,0), shaftwidth=0.2, color=color.red)
y_axis = arrow(pos=vec(0,0,0), axis=vec(0,15,0), shaftwidth=0.2, color=color.green)
z_axis = arrow(pos=vec(0,0,0), axis=vec(0,0,15), shaftwidth=0.2, color=color.blue)


ball = sphere(pos=vec(0,10,0))
ball.m = 1
ball.v = vec(2, -2, 0)
ball.a = vec(0,0,0)

g = vec(0,-9.8,0)

t = 0
dt = 0.01

x1 = vec(ball.pos)
while True:
    rate(1/dt)

    ball.v += ball.a*dt
    ball.pos += ball.v*dt

    if(ball.pos.y<0):
        break

    t += dt

x2 = vec(ball.pos)

W = (ball.m*mag(g))*(mag(x2-x1))*(cos(diff_angle(g, ball.v)))
print('W =',W)