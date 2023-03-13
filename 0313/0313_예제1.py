from vpython import *

# 크기 조정을 위한 변수
scale_factor = 5

# 지구와 달 사이의 거리
r = 384400000

# 만유인력 상수 N*m^2/kg^2
G = 6.67e-11

earth = sphere(pos=vec(0, 0, 0), radius=6371000 *
               scale_factor, texture=textures.earth)
earth.mass = 5.974e24

moon = sphere(pos=vec(r, 0, 0), radius=1737000*scale_factor)
moon.mass = 7347e22

F = G*moon.mass*earth.mass/r**2

earth.force = F
moon.force = F

earth.acc = F/earth.mass
moon.acc = F/moon.mass
