from vpython import *

spring = helix(pos=vec(0, 0, 0), axis=vec(0.2, 0, 0),
               thickness=0.03, coils=10, radius=0.07)
l0 = 0.2
ks = 500

obj = box(pos=vec(3, 0, 0), size=vec(0.3, 0.3, 0.3), color=color.red)
obj.v = vec(-1, 0, 0)
obj.m = 2
obj.collision = False

dt = 0.001
t = 0

while(t < 5):
    rate(1/dt)

    obj.pos += obj.v*dt
    if(obj.pos.x-0.15 <= 0.2):
        obj.collision = True

    if(obj.collision):
        x = l0-spring.axis.x
        F = ks*x
        obj.v += vec(F/obj.m, 0, 0)*dt
        spring.axis = vec(obj.pos.x-0.15, 0, 0)

        if(mag(obj.v) < 0.03):
            print('압축된 길이 :', x)
            break

    t += dt

d = 1*sqrt(obj.m/ks)
print('이론상으로 구한 압축된 길이 :', d)
