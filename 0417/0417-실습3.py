from vpython import *

sun = sphere(pos=vec(0, 0, 0), radius=3.5e10, color=color.red)
mercury = sphere(pos=vec(5.8e10, 0, 0), radius=2.4e9,
                 color=color.white, make_trail=True)
jupiter = sphere(pos=vec(-1.1e11, 0, 0), radius=6e9,
                 color=color.orange, make_trail=True)
earth = sphere(pos=vec(0, 1.5e11, 0), radius=6.4e9,
               texture=textures.earth, make_trail=True)

sun.mass = 1.99e30
mercury.mass = 3.30e23
jupiter.mass = 4.87e24
earth.mass = 5.97e24

sun.v = vec(0, 0, 0)
mercury.v = vec(0, 47630, 0)
jupiter.v = vec(0, -35020, 0)
earth.v = vec(-29783, 0, 0)

G = 6.67e-11

t = 0
dt = 3600*24

while(True):
    rate(60)

    Fsm = G*sun.mass*mercury.mass / \
        mag(mercury.pos-sun.pos)**2*norm(mercury.pos-sun.pos)
    Fsj = G*sun.mass*jupiter.mass / \
        mag(jupiter.pos-sun.pos)**2*norm(jupiter.pos-sun.pos)
    Fse = G*sun.mass*earth.mass / \
        mag(earth.pos-sun.pos)**2*norm(earth.pos-sun.pos)

    Fmj = G*jupiter.mass*mercury.mass / \
        mag(jupiter.pos-mercury.pos)**2*norm(jupiter.pos-mercury.pos)
    Fme = G*earth.mass*mercury.mass / \
        mag(earth.pos-mercury.pos)**2*norm(earth.pos-mercury.pos)

    Fje = G*jupiter.mass*earth.mass / \
        mag(earth.pos-jupiter.pos)**2*norm(earth.pos-jupiter.pos)

    mercury.f = -Fsm+Fmj+Fme
    jupiter.f = -Fsj-Fmj+Fje
    earth.f = -Fse-Fme-Fje

    mercury.v += (mercury.f/mercury.mass)*dt
    jupiter.v += (jupiter.f/jupiter.mass)*dt
    earth.v += (earth.f/earth.mass)*dt

    mercury.pos += mercury.v*dt
    jupiter.pos += jupiter.v*dt
    earth.pos += earth.v*dt

    t += dt
