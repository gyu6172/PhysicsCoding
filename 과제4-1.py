from vpython import *

x_axis = arrow(pos=vec(0,0,0), axis=vec(15,0,0), shaftwidth=0.2, color=color.red)
y_axis = arrow(pos=vec(0,0,0), axis=vec(0,15,0), shaftwidth=0.2, color=color.green)
z_axis = arrow(pos=vec(0,0,0), axis=vec(0,0,15), shaftwidth=0.2, color=color.blue)


ball = sphere(pos=vec(0,10,0))
ball.m = 1
ball.speed = 2
ball.v = vec(ball.speed, 0, 0)
ball.a = 0.2*cross(ball.v, vec(0,0,1))

g=vec(0,-9.8,0)

t = 0
dt = 0.001
W = 0

while True:
    rate(1/dt)

    x1 = vec(ball.pos)
    ball.a = 0.2*cross(ball.v, vec(0,0,1))
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    x2 = vec(ball.pos)

    W += dot(ball.m*g, x2-x1)

    if(ball.pos.y<0):
        break

    t += dt

print('W =',W)
