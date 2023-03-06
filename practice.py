from vpython import *


# Objects

ceiling = box(size=vector(0.3, 0.01, 0.3))

ball1 = sphere(pos=vector(0.0, -0.3, 0.0), radius=0.03, texture=textures.metal,
               make_trail=True, trail_color=color.blue, retain=50)

spring1 = helix(pos=ceiling.pos, axis=ball1.pos-ceiling.pos,
                color=color.black, thickness=.003, coils=30, radius=0.01)


ball2 = sphere(pos=spring1.axis + ball1.pos, radius=0.03,
               texture=textures.metal, make_trail=True, trail_color=color.red, retain=50)

spring2 = helix(pos=ball1.pos, axis=ball2.pos - ball1.pos,
                color=color.black, thickness=.003, coils=30, radius=0.01)


# constants and physical properties

# ball1

g = 9.8

ball1.m = 1

l01 = 0.3

ks1 = 100

kd1 = 1.0

# ball2

l02 = 0.3

ball2.m = 1

ks2 = 100

kd2 = 1.0


# initial values

ball1.v = vector(0, 0, 0)

ball2.v = vector(0, 0, 0)


Fgrav1 = (ball1.m+ball2.m) * vector(0, -g, 0)

Fgrav2 = ball2.m * vector(0, -g, 0)

# time setting

t = 0

dt = 0.01


# the display

scene.background = color.white

scene.autoscale = True

scene.center = vector(0, -l01, 0)

scene.waitfor('click')


# Graph

motion_graph = graph(title='Motion graph', xtitle='time',
                     ytitle='spring length')

traj = gcurve(color=color.blue)

traj2 = gcurve(color=color.red)


# Simulation loop

while True:

    rate(1/dt)  # Real time

    # Spring1 force

    l1 = mag(ball1.pos - ceiling.pos)

    s1 = l1 - l01

    lhat1 = norm(ball1.pos)

    Fspr1 = -ks1 * s1 * lhat1

    # Spring2 force

    l2 = mag(ball2.pos - ball1.pos)

    s2 = l2 - l02

    lhat2 = norm(ball2.pos)

    Fspr2 = -ks2 * s2 * lhat2

    # Damping force for ball1

    Fdamp1 = -kd1 * dot(ball1.v, lhat1) * lhat1

    # Damping force for ball2

    Fdamp2 = -kd2 * dot(ball2.v, lhat2) * lhat2

    # Total force for ball1 and ball2

    Fnet1 = Fgrav1 + Fspr1 + Fdamp1
    Fnet2 = Fgrav2 + Fspr2 + Fdamp2

    # time stepping

    ball1.v = ball1.v + (Fnet1)/ball1.m*dt

    ball1.pos = ball1.pos + ball1.v*dt

    spring1.axis = ball1.pos - ceiling.pos

    ball2.v = ball2.v + Fnet2/ball2.m*dt

    ball2.pos = ball2.pos + ball2.v*dt

    spring2.pos = ball1.pos

    spring2.axis = ball2.pos - ball1.pos

    t = t + dt

    # graph

    traj.plot(pos=(t, l1))

    traj2.plot(pos=(t, l2))
