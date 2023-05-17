from vpython import *

ceiling = box(pos=vec(0, 0, 0), size=vec(0.5, 0.01, 0.5))
board = box(pos=vec(0, -0.25, 0), size=vec(0.4, 0.05, 0.4))

spring1 = helix(pos=vec(-0.09, 0, 0), axis=board.pos - ceiling.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)
spring2 = helix(pos=vec(-0.03, 0, 0), axis=board.pos - ceiling.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)
spring3 = helix(pos=vec(0.03, 0, 0), axis=board.pos - ceiling.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)
spring4 = helix(pos=vec(0.09, 0, 0), axis=board.pos - ceiling.pos,
                color=color.cyan, thickness=0.003, coils=40, radius=0.015)

board.v = vec(0, 0, 0)
g = vec(0, -9.8, 0)
board.m = 1

r0 = 0.25
ks = 100

kv = 0

t = 0
dt = 0.001

scene.autoscale = True
scene.center = vec(0, -r0, 0)

gp = graph(xtitle='t', ytitle='pos')
traj = gcurve(color=color.red)


while t < 20:
    rate(1/dt)

    Fgrav = board.m*g
    r = mag(board.pos-ceiling.pos)
    s = r - r0
    rhat = norm(board.pos-ceiling.pos)
    Fspr = -ks*s*rhat
    Fdamp = -kv*dot(board.v, rhat)*rhat
    Fnet = Fgrav + Fspr*4 + Fdamp*4

    board.v = board.v + Fnet/board.m*dt
    board.pos = board.pos + board.v*dt

    t += dt

    spring1.axis = board.pos-ceiling.pos
    spring2.axis = board.pos-ceiling.pos
    spring3.axis = board.pos-ceiling.pos
    spring4.axis = board.pos-ceiling.pos

    traj.plot(pos=(t, board.pos.y))
