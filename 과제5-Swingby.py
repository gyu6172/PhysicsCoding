from vpython import *


def initPlanet(p, m, r):
    planet = sphere(pos=p, radius=r)
    planet.m = m
    return planet


def updateForce(ball, planet):
    global G
    r = planet.pos - ball.pos
    ball.f = G*ball.m*planet.m/mag(r)**2*norm(r)


def updatePos(ball, dt):
    ball.v += ball.f/ball.m*dt
    ball.pos += ball.v*dt


def on_keydown(event):
    global shoot_arrow
    global ball
    global gamestate

    if (event.key == "up" and shoot_arrow.theta < 90):
        shoot_arrow.theta += 1
    elif (event.key == "down" and shoot_arrow.theta > -90):
        shoot_arrow.theta -= 1
    elif (event.key == "right"):
        shoot_arrow.r += 10
    elif (event.key == "left" and shoot_arrow.r > 0):
        shoot_arrow.r -= 10
    elif (event.key == "shift"):
        ball.visible = True
        gamestate['ready'] = False
        gamestate['shoot'] = True


x_axis = arrow(pos=vec(0, 0, 0), axis=vec(
    5000, 0, 0), shaftwidth=30, color=color.red)
y_axis = arrow(pos=vec(0, 0, 0), axis=vec(0, 5000, 0),
               shaftwidth=30, color=color.green)
#z_axis = arrow(pos=vec(0,0,0), axis=vec(0,0,5000), shaftwidth = 30, color=color.blue)

planet_list = []
m = 5e19
planet_list.append(initPlanet(vec(1300, -100, 0), m, 100))
planet_list.append(initPlanet(vec(1700, 300, 0), m, 100))
planet_list.append(initPlanet(vec(2000, -400, 0), m, 100))
planet_list.append(initPlanet(vec(2500, 500, 200), m, 100))

earth = sphere(pos=vec(3200, 0, 0), radius=150, texture=textures.earth)

shoot_arrow = arrow(pos=vec(0, 0, 0), axis=vec(
    500, 0, 0), shaftwidth=40, color=color.yellow)
shoot_arrow.theta = 45
shoot_arrow.r = 500

ball = sphere(pos=vec(0, 0, 0), radius=30, color=color.red,
              make_trail=True, visible=False)
ball.v = vec(2*shoot_arrow.r*cos(radians(shoot_arrow.theta)),
             2*shoot_arrow.r*sin(radians(shoot_arrow.theta)), 0)
ball.f = vec(0, 0, 0)
ball.m = 100

scene.bind("keydown", on_keydown)

gamestate = {'ready': True, 'shoot': False}

G = 6.67e-11

t = 0
dt = 0.001

while True:
    rate(1/dt)

    if (gamestate['ready']):
        shoot_arrow.axis = vec(shoot_arrow.r*cos(radians(shoot_arrow.theta)),
                               shoot_arrow.r*sin(radians(shoot_arrow.theta)), 0)
        ball.v = vec(2*shoot_arrow.r*cos(radians(shoot_arrow.theta)),
                     2*shoot_arrow.r*sin(radians(shoot_arrow.theta)), 0)

    elif (gamestate['shoot']):

        for planet in planet_list:
            updateForce(ball, planet)

        updatePos(ball, dt)

    t += dt
