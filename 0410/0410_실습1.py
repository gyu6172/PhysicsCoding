from vpython import *

global R, W
R = 1
W = 2


def r(t):
    return vec(R*cos(W*t), R*sin(W*t), 0)


def v(t):
    return vec(-R*W*sin(W*t), R*W*cos(W*t), 0)


def a(t):
    return vec(-R*W*W*cos(W*t), -R*W*W*sin(W*t), 0)


rArrow = arrow(pos=vec(0, 0, 0), color=color.red, shaftwidth=0.2)
vArrow = arrow(pos=vec(0, 0, 0), color=color.green, shaftwidth=0.2)
aArrow = arrow(pos=vec(0, 0, 0), color=color.blue, shaftwidth=0.2)

t = 0
dt = 0.01
while(t < 10):
    rate(1/dt)
    rArrow.axis = r(t)
    vArrow.axis = v(t)
    aArrow.axis = a(t)

    t += dt
