from vpython import *
import random


def on_keydown(event):
    global airplane
    if (event.key == "left" and airplane.pos.x > -9):
        airplane.pos.x -= 0.5
    elif (event.key == "right" and airplane.pos.x < 9):
        airplane.pos.x += 0.5
    elif (event.key == "up" and airplane.pos.y > -9):
        airplane.pos.y += 0.5
    elif (event.key == "down" and airplane.pos.y < 9):
        airplane.pos.y -= 0.5


bulletList = list()

# 총알 추가
for i in range(7):
    bullet = sphere(pos=vec(random.randrange(0, 18)-9, 9, 0),
                    radius=0.5, color=color.red)
    bullet.v = vec(0, random.randrange(0, 10)-15, 0)
    bulletList.append(bullet)

# 비행기 추가
airplane = box(pos=vec(0, -8, 0), size=vec(1, 1, 1))

# scene = canvas(width=800, height=600)
# scene.range = 10
# scene.title = "Dodge Game"
scene.bind("keydown", on_keydown)

t = 0
dt = 0.01
gameover = False

while(not gameover):
    rate(1/dt)
    for bullet in bulletList:
        bullet.pos += bullet.v*dt
        if(bullet.pos.y < -9):
            bullet.pos.y = 9
            bullet.v = vec(0, random.randrange(0, 10)-15, 0)
        if((bullet.pos.x-0.5 < airplane.pos.x and airplane.pos.x < bullet.pos.x+0.5) and (bullet.pos.y-0.5 < airplane.pos.y and airplane.pos.y < bullet.pos.y+0.5)):
            gameover = True
            continue

    t += dt
