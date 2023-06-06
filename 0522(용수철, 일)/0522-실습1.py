from vpython import *


def F(x):
    return 1+0.8*x
    # return 1+0.16*x**2


car = box(pos=vec(0, 0, 0), size=vec(0.2, 0.2, 0.2), color=color.red)
line = box(pos=vec(5, 0, 0), size=vec(0.01, 3, 3))
car.m = 1
car.v = vec(0, 0, 0)
car.a = vec(0, 0, 0)


dt = 0.001
t = 0
W = 0
while(car.pos.x < 5):
    rate(1/dt)

    car.v += (vec(F(car.pos.x), 0, 0)/car.m)*dt
    car.pos += car.v*dt
    W += dot(car.v, vec(F(car.pos.x), 0, 0))*dt
    t += dt

print('속력 :', car.v)
print('운동에너지 :', 0.5*car.m*car.v.x**2)
print('W :', W)
