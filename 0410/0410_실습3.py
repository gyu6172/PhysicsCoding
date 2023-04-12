from vpython import *

ball = sphere(pos=vec(0, 0, 0), radius=0.2, color=color.red)
ball.v = vec(2, 0, 0)
ball.a = vec(2, 0, 0)

xaxis = arrow(pos=vec(0, 0, 0), axis=vec(5, 0, 0),
              shaftwidth=0.2, color=color.red)
yaxis = arrow(pos=vec(0, 0, 0), axis=vec(0, 5, 0),
              shaftwidth=0.2, color=color.green)
zaxis = arrow(pos=vec(0, 0, 0), axis=vec(0, 0, 5),
              shaftwidth=0.2, color=color.blue)

e3 = vec(0, 0, -1)
x1 = ball.pos

motion_ball = graph(xtitle="t", ytitle="ball.pos.y")
g_ball = gcurve(graph=motion_ball)

t = 1
dt = 0.001
while(t < 20):
    rate(1/dt)
    ball.a = 2*norm(cross(ball.v, e3))
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    g_ball.plot(pos=(t, ball.pos.y))
    t += dt
