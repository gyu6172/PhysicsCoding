from vpython import *

earth = sphere(pos=vec(0, 1.5e11, 0), radius=6.4e9,
               texture=textures.earth, make_trail=True)
sun = sphere(pos=vec(0, 0, 0), color=color.red, radius=3.5e10)
earth.mass = 5.97e24
sun.mass = 1.99e30


earth.v = vec(-29783, 0, 0)
sun.v = vec(0, 0, 0)

G = 6.67e-11

t = 0
dt = 3600*24

x1 = vec(0, 1.5e11, 0)
flag = 0
while(True):
    rate(60)
    r = earth.pos - sun.pos

    earth.f = -G*earth.mass*sun.mass/mag(r)**2*norm(r)
    sun.f = -earth.f

    earth.v += (earth.f/earth.mass) * dt
    sun.v += (sun.f/sun.mass) * dt
    earth.pos += earth.v * dt
    sun.pos += sun.v * dt
    if(mag(earth.pos-x1) < earth.radius and flag == 1):
        flag = 0
        print(t/3600/24, "days")
    if(mag(earth.pos-x1) > earth.radius):
        flag = 1

    t += dt
