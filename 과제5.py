from vpython import *
import random


def initBall(p, r, mass, color):
    ball = sphere(pos=p, radius=r, color=color)
    ball.v = vec(0, 0, 0)
    ball.m = mass
    ball.f = vec(0, 0, 0)
    return ball


def on_keydown(event):
    global shoot
    global gamestate
    print('power =', shoot.power)
    print('theta =', shoot.theta)
    if (event.key == "left"):
        shoot.theta -= 1
    elif (event.key == "right"):
        shoot.theta += 1
    elif (event.key == "up" and shoot.power < 0.8):
        shoot.power += 0.01
    elif (event.key == "down" and shoot.power > 0):
        shoot.power -= 0.01
    elif (event.key == "shift"):
        gamestate['ready'] = False
        gamestate['shoot'] = True


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


def updatePos(ball, dt):
    global g, uk
    ball.f = -uk*ball.m*mag(g)*norm(ball.v)
    ball.v += ball.f/ball.m*dt
    ball.pos += ball.v*dt
    if(mag(ball.v) < 0.001):
        ball.v = vec(0, 0, 0)


x_axis = arrow(pos=vec(0, 0, 0), axis=vec(
    5, 0, 0), shaftwidth=0.03, color=color.red)
y_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 5, 0),
               shaftwidth=0.03, color=color.green)
z_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 0, 5),
               shaftwidth=0.03, color=color.blue)

r = 0.0285
m = 0.17

ball_list = []
color_list = [
    color.yellow,
    color.blue,
    color.red,
    color.green,
    color.black,
    color.orange,
    color.purple,
    color.cyan,
    color.magenta,
    color.yellow,
    color.blue,
    color.red,
    color.green,
    color.orange,
    color.purple,
]

initpos_list = []

for i in range(5):
    for j in range(-i, i+1, 2):
        initpos_list.append(vec(r*j, 0, -sqrt(3)*i*r))

initpos = vec(0, 0, 0.8)
ball_list.append(initBall(initpos, r, m, color.white))

for i in range(1, 16):
    ball_list.append(initBall(initpos_list[i-1], r, m, color_list[i-1]))

w = 1.27
h = 2.54
table = box(pos=vec(0, -r-0.05, 0.5), size=vec(w, 0.1, h), color=color.green)

shoot = arrow(pos=vec(0, 0, 0), color=color.white, shaftwidth=0.005)
shoot.power = 0.2
shoot.theta = 90
shoot.axis = vec(shoot.power*cos(radians(shoot.theta)),
                 0, shoot.power*sin(shoot.theta))

uk = 0.002
g = vec(0, -9.8, 0)

gamestate = {'ready': True, 'shoot': False}

scene.bind("keydown", on_keydown)

t = 0
dt = 0.0001
while True:
    rate(1/dt)

    if(gamestate["ready"]):
        shoot.visible = True
        shoot.axis = vec(shoot.power*sin(radians(shoot.theta)),
                         0, shoot.power*cos(shoot.theta))
        ball_list[0].v = 10*vec(shoot.power*cos(radians(shoot.theta)),
                                0, shoot.power*sin(shoot.theta))

    elif(gamestate['shoot']):
        shoot.visible = False
        for ball in ball_list:
            updatePos(ball, dt)

        for b1 in ball_list:
            for b2 in ball_list:
                if(b1 == b2):
                    continue
                if(isCollision(b1, b2)):
                    updateCollision(b1, b2, 0.9)

    t += dt
