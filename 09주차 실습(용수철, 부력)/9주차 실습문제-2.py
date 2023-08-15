from vpython import *

r = 0.05
tank = box(pos=vec(0, 0, 0), size=vec(5, 5, 5), color=color.blue, opacity=0.5)
stone = sphere(pos=vec(-2.5+r, 0, 0), radius=r, color=color.red)

stone.v = vec(108/3.6, 0, 0)
x0 = stone.pos.x
g = vec(0, -9.8, 0)

pw = 1000  # kg/m^3
ps = 2500  # kg/m^3

stone.m = ps*(4/3*pi*r**3)

cd = 0.5

t = 0
dt = 0.001
x1 = 0

while(t < 10):
    rate(1/dt)

    Fb = -pw*(4/3*pi*r**3)*g
    Fg = stone.m*g
    Fdrag = -0.5*cd*pw*(pi*r**2)*(mag(stone.v)**2)*norm(stone.v)
    F = Fb + Fg + Fdrag

    stone.v = stone.v + F/stone.m*dt
    stone.pos = stone.pos + stone.v*dt

    if(stone.pos.y < -2.5):
        x1 = stone.pos.x
        break
    t += dt

print(t, '초')
print(x1-x0, 'm')
