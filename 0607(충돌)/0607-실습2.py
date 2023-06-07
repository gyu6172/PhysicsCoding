from vpython import *


def isCollision(b1, b2):
    dist = mag(b1.pos - b2.pos)
    if(dist < b1.radius + b2.radius):
        return True
    else:
        return False


def updateCollision(b1, b2, e):
    r = b2.pos - b1.pos
    r_hat = norm(r)
    dist = mag(r)

    v1_c = dot(b1.v, r_hat)*r_hat
    v2_c = dot(b2.v, r_hat)*r_hat
    v1_p = b1.v - v1_c
    v2_p = b2.v - v2_c

    v1 = ((b1.m-e*b2.m)*v1_c + (1+e)*b2.m*v2_c)/(b1.m+b2.m)
    v2 = ((b2.m-e*b1.m)*v2_c + (1+e)*b1.m*v1_c)/(b1.m+b2.m)

    b1.v = v1 + v1_p
    b2.v = v2 + v2_p


white_ball = sphere(pos=vec(0, 0, 0), radius=0.05,
                    color=color.white, make_trail=True)
red_ball = sphere(pos=vec(1, 0.05, 0), radius=0.05,
                  color=color.red, make_trail=True)
green_ball = sphere(pos=vec(1.5, 0.4, 0), radius=0.05,
                    color=color.green, make_trail=True)

white_ball.v = vec(0.3, 0, 0)
red_ball.v = vec(0, 0, 0)
green_ball.v = vec(0, 0, 0)

white_ball.f = vec(0, 0, 0)
red_ball.f = vec(0, 0, 0)
green_ball.f = vec(0, 0, 0)

g = vec(0, 0, -9.8)

white_ball.m = 1
red_ball.m = 1
green_ball.m = 1

uk = 0.002

gp = graph(xtitle='t', ytitle='Central Mass')
central_mass_x = gcurve(graph=gp, color=color.red)
central_mass_y = gcurve(graph=gp, color=color.blue)

t = 0
dt = 0.001

while True:
    rate(1/dt)

    if(isCollision(white_ball, red_ball)):
        updateCollision(white_ball, red_ball, 1)

    if(isCollision(red_ball, green_ball)):
        updateCollision(red_ball, green_ball, 1)

    white_ball.f = -uk*white_ball.m*mag(g)*norm(white_ball.v)
    red_ball.f = -uk*red_ball.m*mag(g)*norm(red_ball.v)
    green_ball.f = -uk*green_ball.m*mag(g)*norm(green_ball.v)

    white_ball.v += white_ball.f/white_ball.m*dt
    red_ball.v += red_ball.f/red_ball.m*dt
    green_ball.v += green_ball.f/green_ball.m*dt

    white_ball.pos += white_ball.v*dt
    red_ball.pos += red_ball.v*dt
    green_ball.pos += green_ball.v*dt

    v_com = (white_ball.m*white_ball.v + red_ball.m*red_ball.v +
             green_ball.m*green_ball.v)/(white_ball.m+red_ball.m+green_ball.m)

    central_mass_x.plot(pos=(t, v_com.x))
    central_mass_y.plot(pos=(t, v_com.y))

    if(mag(white_ball.v) < 0.01):
        white_ball.v = vec(0, 0, 0)
    if(mag(red_ball.v) < 0.01):
        red_ball.v = vec(0, 0, 0)
    if(mag(green_ball.v) < 0.01):
        green_ball.v = vec(0, 0, 0)

    t += dt
