from vpython import *

r = 0.5

p1 = sphere(pos=vec(0, 0, 0), radius=0.1, color=color.white)
p2 = sphere(pos=vec(r, 0, 0), radius=0.1, color=color.red)

p1.mass = 80
p2.mass = 60

# 만유인력 상수
G = 6.67e-11  # N*m^2/kg^2

F = G*p1.mass*p2.mass/r**2

p1.force = -F
p2.force = F

p1.acc = F/p1.mass
p2.acc = F/p2.mass

print('p1.force = ', end='')
print(p1.force, "N")
print('p2.force = ', end='')
print(p2.force, "N")

print('p1.acc = ', end='')
print(p1.acc, "m/s^2")
print('p2.acc = ', end='')
print(p2.acc, "m/s^2")
