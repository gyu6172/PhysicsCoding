from vpython import *

A = box(pos=vec(-8, 0, 0), size=vec(2, 1, 1), color=color.red)
B = box(pos=vec(-8, 2, 0), size=vec(2, 1, 1), color=color.blue)

A.v = vec(3, 0, 0)
B.v = vec(0, 0, 0)

B.a = vec(1, 0, 0)

t = 0
dt = 0.001

motion_graph = graph(title='position-time', xtitle='time', ytitle='postion')
APosition = gcurve(color=color.red)
BPosition = gcurve(color=color.blue)

while(A.pos.x >= B.pos.x):
    rate(1/dt)
    A.pos += A.v*dt
    B.pos += B.v*dt

    B.v += B.a*dt

    APosition.plot(pos=(t, A.pos.x))
    BPosition.plot(pos=(t, B.pos.x))

    t += dt

print('time=', t)
print('x=', B.pos.x)
