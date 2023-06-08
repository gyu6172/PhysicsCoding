from vpython import *


def initBall(p, r, mass, color):
    ball = sphere(pos=p, radius=r, color=color)
    ball.v = vec(0, 0, 0)
    ball.m = mass
    ball.f = vec(0, 0, 0)
    return ball


def initPlate(pos, size):
    plate = box(pos=pos, size=size, color=color.green)
    return plate


def on_keydown(event):
    global shoot
    global gamestate
    if (event.key == "left"):
        shoot.theta += 1
    elif (event.key == "right"):
        shoot.theta -= 1
    elif (event.key == "up" and shoot.power < 0.5):
        shoot.power += 0.01
    elif (event.key == "down" and shoot.power > 0):
        shoot.power -= 0.01
    elif (event.key == "shift"):
        gamestate['ready'] = False
        gamestate['shoot'] = True


def collision_ball(b1, b2, e):
    n = b1.pos - b2.pos
    n_hat = norm(n)
    dist = mag(n)
    v_relm = dot(b1.v - b2.v, n_hat)
    if v_relm > 0:
        return False
    tot_radius = b1.radius + b2.radius
    if dist > tot_radius:
        return False
    else:
        j = -(1+e)*v_relm
        j = j/(1/b1.m+1/b2.m)
        b1.v = b1.v + j*n_hat/b1.m
        b2.v = b2.v - j*n_hat/b2.m
        b1.v *= 0.9
        b2.v *= 0.9
        # _Option: Postion correction
        # scene.waitfor('click')
        #print(b1.radius + b2.radius - dist)
        b1.pos = b1.pos + n_hat*(tot_radius - dist)*b2.m/(b1.m + b2.m)
        b2.pos = b2.pos - n_hat*(tot_radius - dist)*b1.m/(b1.m + b2.m)
        #print(b1.radius + b2.radius - mag(b1.pos - b2.pos))
        # scene.waitfor('click')
        return True


def collision_plate(ball, table, e):
    if -table.size.x/2 > ball.pos.x - ball.radius:
        ball.pos.x = -table.size.x/2 + ball.radius
        ball.v.x = -e*ball.v.x

    if table.size.x/2 < ball.pos.x + ball.radius:
        ball.pos.x = table.size.x/2 - ball.radius
        ball.v.x = -e*ball.v.x

    if -table.size.z/2 > ball.pos.z - ball.radius:
        ball.pos.z = -table.size.z/2 + ball.radius
        ball.v.z = -e*ball.v.z

    if table.size.z/2 < ball.pos.z + ball.radius:
        ball.pos.z = table.size.z/2 - ball.radius
        ball.v.z = -e*ball.v.z


def collisionHole(ball, hole):
    global hole_r

    if(mag(ball.pos - hole) < hole_r):
        return True
    else:
        return False


def updatePos(ball, dt):
    global g, uk
    ball.f = -uk*ball.m*mag(g)*norm(ball.v)
    ball.v += ball.f/ball.m*dt
    ball.pos += ball.v*dt
    if(mag(ball.v) < 0.01):
        ball.v = vec(0, 0, 0)


# x_axis = arrow(pos=vec(0, 0, 0), axis=vec(5, 0, 0),
#                shaftwidth=0.03, color=color.red)
# y_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 5, 0),
#                shaftwidth=0.03, color=color.green)
# z_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 0, 5),
#                shaftwidth=0.03, color=color.blue)

r = 0.0285
m = 0.017

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
        initpos_list.append(vec(r*j, 0, -sqrt(3)*i*r-0.3))

initpos = vec(0, 0, 0.8)
ball_list.append(initBall(initpos, r, m, color.white))

for i in range(1, 16):
    ball_list.append(initBall(initpos_list[i-1], r, m, color_list[i-1]))

w = 1.27
h = 2.54
table = box(pos=vec(0, -r-0.05, 0), size=vec(w, 0.1, h), color=color.green)

plate_list = []

hole_r = 0.07
pw = w-2*hole_r
ph = 0.1
pt = 0.001

plate_list.append(initPlate(vec(0, 0, -h/2), vec(pw, ph, pt)))
plate_list.append(initPlate(vec(0, 0, h/2), vec(pw, ph, pt)))
plate_list.append(initPlate(vec(w/2, 0, h/4), vec(pt, ph, pw)))
plate_list.append(initPlate(vec(w/2, 0, -h/4), vec(pt, ph, pw)))
plate_list.append(initPlate(vec(-w/2, 0, h/4), vec(pt, ph, pw)))
plate_list.append(initPlate(vec(-w/2, 0, -h/4), vec(pt, ph, pw)))

hole_list = []
hole_list.append(vec(w/2, 0, h/2))
hole_list.append(vec(w/2, 0, 0))
hole_list.append(vec(w/2, 0, -h/2))
hole_list.append(vec(-w/2, 0, h/2))
hole_list.append(vec(-w/2, 0, 0))
hole_list.append(vec(-w/2, 0, -h/2))

shoot = arrow(pos=ball_list[0].pos, color=color.white, shaftwidth=0.005)
shoot.power = 0.3
shoot.theta = -180
shoot.axis = vec(shoot.power*sin(radians(shoot.theta)),
                 0, shoot.power*cos(radians(shoot.theta)))

uk = 0.02
g = vec(0, -9.8, 0)

gamestate = {'ready': True, 'shoot': False,
             'gameover': False, 'gamelose': False, 'gamewin': False}

scene.bind("keydown", on_keydown)

t = 0
dt = 0.001
while not gamestate['gameover']:
    rate(1/dt)

    # for ar in arrow_list:
    #     for plate in plate_list:
    #         ar.axis = ball_list[0].pos-plate.pos

    if(gamestate['ready']):
        scene.center = ball_list[0].pos
        shoot.pos = ball_list[0].pos
        shoot.visible = True
        shoot.axis = vec(shoot.power*sin(radians(shoot.theta)),
                         0, shoot.power*cos(radians(shoot.theta)))
        ball_list[0].v = 10*vec(shoot.power*sin(radians(shoot.theta)),
                                0, shoot.power*cos(radians(shoot.theta)))

    elif(gamestate['shoot']):
        shoot.visible = False

        if (len(ball_list) == 1):
            gamestate['gamewin'] = True
            gamestate['gameover'] = True

        for ball in ball_list:
            updatePos(ball, dt)

        for b1 in ball_list:
            for b2 in ball_list:
                if(b1 == b2):
                    continue
                collision_ball(b1, b2, 1)

        for ball in ball_list:
            collision_plate(ball, table, 0.9)

        for ball in ball_list:
            for hole in hole_list:
                if(collisionHole(ball, hole)):
                    if(ball == ball_list[0]):
                        gamestate['gameover'] = True
                        gamestate['gamelose'] = True
                        ball.visible = False

                    else:
                        ball.visible = False
                        ball_list.remove(ball)

        flag = True
        for ball in ball_list:
            if(mag(ball.v) > 0.01):
                flag = False

        if(flag):
            gamestate['ready'] = True
            gamestate['shoot'] = False

    t += dt

gameover_text = label(pos=ball_list[0].pos, height=30)
if(gamestate['gamelose']):
    gameover_text.text = "Game Over!"
elif(gamestate['gamewin']):
    gameover_text.text = "You Win!"
