from vpython import *
# 실습2 : u값을 0.25로 바꾸기


def setVelocity():
    car.speed = velocitySlider.value
    car.v = vec(car.speed, 0, 0)


def startBtn(b):
    b.disabled = True
    return b.disabled


init_pos = vec(0, 0, 0)
car = box(pos=init_pos)
car.speed = 0
car.v = vec(0, 0, 0)
car.f = vec(0, 0, 0)
car.m = 300
u = 0.8
g = 9.8
person = sphere(pos=vec(40, 0, 0))

velocitySlider = slider(min=0, max=50, value=25, bind=setVelocity)
startBtn = button(text="start", bind=startBtn)

t = 0
dt = 0.001
flag = 0

# 최소속력 : a=-u*g일때 20m를 가는 속력
# (v1)^2 - (v0)^2 = 2*(-u*g)*S
# v0 = sqrt(2*u*g*20)
#즉, v0 = 17.7
crash = text(pos=vec(0, 0, 0), text="crash")
crash.visible = False

while(True):
    rate(1/dt)

    if startBtn.disabled == True:
        if flag == 0:
            print(car.speed, 'm/s')
            flag = 1

        car.pos += car.v*dt

        if car.pos.x > 20:
            car.f = vec(-u*g*car.m, 0, 0)
            car.v += (car.f/car.m)*dt

        t += dt

        if car.v.x < 0 or car.pos.x > person.pos.x:
            if(car.pos.x > person.pos.x):
                crash.visible = True
            scene.waitfor('click')
            startBtn.disabled = False
            car.pos = init_pos
            car.v = vec(0, 0, 0)
            car.f = vec(0, 0, 0)
            crash.visible = False
            car.speed = 0
            flag = 0
            t = 0
