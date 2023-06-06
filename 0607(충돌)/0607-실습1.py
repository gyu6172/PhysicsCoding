from vpython import *


def collision(b1, b2, e):
    dist = mag(b1.pos - b2.pos)
    tot_m = b1.m + b2.m


white_ball = sphere(pos=vec(0, 0, 0), radius=0.05, color=color.white)
red_ball = sphere(pos=vec(1, 0.05, 0), radius=0.05, color=color.red)
green_ball = sphere(pos=vec(1.5, 0.4, 0), radius=0.05, color=color.green)

white_ball.v = vec(0.3, 0, 0)
red_ball.v = vec(0, 0, 0)
green_ball.v = vec(0, 0, 0)

white_ball.m = 1
red_ball.m = 1
green_ball.m = 1

t = 0
dt = 0.0001

while True:
    rate(1/dt)

    t += dt
