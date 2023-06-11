from vpython import *

door = box(pos=vec(0,0,0), size=vec(0.8, 2, 0.1))
door.m = 40

handle = sphere(pos=vec(0.35, 0, 0), radius=0.06, color=color.red)

t = 0
dt = 0.01

theta = 0

F = vec(0,0,-10) #N

tmp = arrow(pos=vec(-0.4, -1, 0), axis=vec(0, 2, 0), shaftwidth=0.02, color=color.blue)

r = 0.75

door.w = vec(0,0,0)
door.alpha = F/door.m/r

while True:
    rate(1/dt)

    door.w = door.alpha*dt

    dtheta = mag(door.w)*dt

    door.rotate(angle = dtheta, axis = tmp.axis, origin = tmp.pos)
    handle.rotate(angle = dtheta, axis = tmp.axis, origin = tmp.pos)
    theta += dt*0.01

    t += dt