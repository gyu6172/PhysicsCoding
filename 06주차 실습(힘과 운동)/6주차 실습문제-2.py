from vpython import *
r = 3
planet = sphere(pos=vec(0, 0, 0), radius=r)
prince = sphere(pos=vec(0, 4, 0), radius=0.1)

# 지구 질량
M = 5.97e24
# 중력상수
G = 6.67e-11
# 지구 반지름
R = 6371000

# 지구 중력가속도
g = G*M/R**2

# (지구 중력가속도) = (어린왕자 행성 중력가속도)
#g = G*planet.m/r^2
planet.m = g*r**2/G
print('Mass of the planet :', planet.m, 'kg')

Ffoot = G*planet.m/(planet.radius)**2
Fhead = G*planet.m/(planet.radius+1)**2
print('Gravitational acceleration difference :', abs(Fhead-Ffoot), 'm/s^2')

#공전속도 : sqrt(GM/R)
#prince.v = vec(sqrt(G*planet.m/(r+1)), 0, 0)
prince.v = vec(sqrt((r+1)*(G*planet.m/(r+1)**2)), 0, 0)
prince.a = vec(0, -Fhead, 0)
print('Velocity :', mag(prince.v), 'm/s')

t = 0
dt = 0.001
while(True):
    rate(1/dt)

    prince.a = norm(planet.pos-prince.pos)*(mag(prince.a))
    prince.v += prince.a*dt

    prince.pos += prince.v*dt

    t += dt
