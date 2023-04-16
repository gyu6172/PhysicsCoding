from vpython import *
stone = sphere(pos=vec(0, 0, 0), radius=0.5, color=color.white)
monkey = sphere(pos=vec(12, 9, 0), radius=0.5, color=color.orange)

stone.v = vec(9.6, 7.2, 0)
monkey.v = vec(0, 0, 0)

stone.a = vec(0, -9.8, 0)
monkey.a = vec(0, -9.8, 0)

t = 0
dt = 0.001

while(True):
    rate(1/dt)
    stone.v += stone.a*dt
    monkey.v += monkey.a*dt
    stone.pos += stone.v*dt
    monkey.pos += monkey.v*dt
    if(mag(monkey.pos - stone.pos) < stone.radius):
        break

    t += dt
