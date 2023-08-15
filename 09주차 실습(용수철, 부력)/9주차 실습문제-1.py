from vpython import *

ceiling1 = box(pos=vec(-1, 0, 0), size=vec(0.2, 0.01, 0.2))
ball1 = sphere(pos=vec(-1.0, -0.25, 0.0), radius=0.025,
               color=color.orange, make_trail=True)
spring1 = helix(pos=ceiling1.pos, axis=ball1.pos - ceiling1.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)

ceiling2 = box(pos=vec(0, 0, 0), size=vec(0.2, 0.01, 0.2))
ball2 = sphere(pos=vec(0.0, -0.25, 0.0), radius=0.025,
               color=color.orange, make_trail=True)
spring2 = helix(pos=ceiling2.pos, axis=ball2.pos - ceiling2.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)

ceiling3 = box(pos=vec(1, 0, 0), size=vec(0.2, 0.01, 0.2))
ball3 = sphere(pos=vec(1.0, -0.25, 0.0), radius=0.025,
               color=color.orange, make_trail=True)
spring3 = helix(pos=ceiling3.pos, axis=ball3.pos - ceiling3.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)

ball1.v = vec(0, 0, 0)
ball2.v = vec(0, 0, 0)
ball3.v = vec(0, 0, 0)

g = vec(0, -9.8, 0)
ball1.m = 1
ball2.m = 1
ball3.m = 1

r0 = 0.25
ks = 100

kv1 = 0.5
kv2 = 1
kv3 = 2

t = 0
dt = 0.001

scene.autoscale = True
scene.center = vec(0, -r0, 0)

gp = graph(xtitle='t', ytitle='pos')
traj1 = gcurve(color=color.red)
traj2 = gcurve(color=color.green)
traj3 = gcurve(color=color.blue)

while t < 10:
    rate(1/dt)

    Fgrav1 = ball1.m*g
    r1 = mag(ball1.pos-ceiling1.pos)
    s1 = r1 - r0
    rhat1 = norm(ball1.pos-ceiling1.pos)
    Fspr1 = -ks*s1*rhat1
    Fdamp1 = -kv1*dot(ball1.v, rhat1)*rhat1
    Fnet1 = Fgrav1 + Fspr1 + Fdamp1

    Fgrav2 = ball2.m*g
    r2 = mag(ball2.pos-ceiling2.pos)
    s2 = r2 - r0
    rhat2 = norm(ball2.pos - ceiling2.pos)
    Fspr2 = -ks*s2*rhat2
    Fdamp2 = -kv2*dot(ball2.v, rhat2)*rhat2
    Fnet2 = Fgrav2 + Fspr2 + Fdamp2

    Fgrav3 = ball3.m*g
    r3 = mag(ball3.pos - ceiling3.pos)
    s3 = r3 - r0
    rhat3 = norm(ball3.pos - ceiling3.pos)
    Fspr3 = -ks*s3*rhat3
    Fdamp3 = -kv3*dot(ball3.v, rhat3)*rhat3
    Fnet3 = Fgrav3 + Fspr3 + Fdamp3

    ball1.v = ball1.v + Fnet1/ball1.m*dt
    ball1.pos = ball1.pos + ball1.v*dt

    ball2.v = ball2.v + Fnet2/ball2.m*dt
    ball2.pos = ball2.pos + ball2.v*dt

    ball3.v = ball3.v + Fnet3/ball3.m*dt
    ball3.pos = ball3.pos + ball3.v*dt

    t += dt

    spring1.axis = ball1.pos-ceiling1.pos
    spring2.axis = ball2.pos-ceiling2.pos
    spring3.axis = ball3.pos-ceiling3.pos

    traj1.plot(pos=(t, ball1.pos.y))
    traj2.plot(pos=(t, ball2.pos.y))
    traj3.plot(pos=(t, ball3.pos.y))
