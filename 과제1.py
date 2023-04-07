from vpython import *
import random as rand


def on_keydown(event):
    global airplane
    if (event.key == "left" and airplane.pos.x > -9):
        airplane.pos.x -= 0.5
    elif (event.key == "right" and airplane.pos.x < 9):
        airplane.pos.x += 0.5
    elif (event.key == "up" and airplane.pos.y < 9):
        airplane.pos.y += 0.5
    elif (event.key == "down" and airplane.pos.y > -9):
        airplane.pos.y -= 0.5


bulletList = list()

# 총알 추가
for i in range(7):
    bullet = sphere(pos=vec(rand.uniform(-9, 9), 9, 0),
                    radius=0.5, color=color.red)
    bullet.v = vec(0, rand.uniform(-20, -10), 0)
    bulletList.append(bullet)

# 비행기 추가
airplane = box(pos=vec(0, -8, 0), size=vec(1, 1, 1))

timeText = label(pos=vec(-9, 9, 0))
gameoverText = label(color=color.red, height=30, box=False)

scene.range = 10
scene.title = "Dodge Game"
scene.bind("keydown", on_keydown)
scene = canvas(pos=vec(0, 0, 0), width=800, height=600)

t = 0
dt = 0.01
gameover = False

while(not gameover):
    rate(1/dt)
    for bullet in bulletList:
        bullet.pos += bullet.v*dt
        if(bullet.pos.y < -9):
            bullet.pos.y = 9
            bullet.pos.x = rand.uniform(-9, 9)
            bullet.v = vec(0, rand.uniform(-20, -10), 0)
        if(mag(bullet.pos - airplane.pos) <= 1):
            gameover = True
            gameoverText.text = "Game Over!"
            continue
    timeText.text = "{:.2f}".format(t)

    t += dt
