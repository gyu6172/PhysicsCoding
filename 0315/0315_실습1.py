from vpython import *


# 지구객체 생성
earth = sphere(pos=vec(0, 0, 0), radius=6371000, texture=textures.earth)

# 지구와 사과 사이의 거리
d = earth.radius*1.1

# 사과 객체 생성
apple = sphere(pos=vec(0, d, 0), radius=300000, color=color.red)

# 지구의 질량
earth.mass = 5.974e24  # kg

# 사과의 질량
apple.mass = 0.07  # kg

# 만유인력 상수
G = 6.67e-11  # N*m^2/kg^2

# 만유인력
F = G*earth.mass*apple.mass/d**2

# 둘 사이의 작용하는 만유인력
earth.force = -F
apple.force = F

# 지구와 사과의 가속도 구하기
earth.acc = F/earth.mass
apple.acc = F/apple.mass

print('earth.force = ', end='')
print(earth.force, "N")
print('apple.force = ', end='')
print(apple.force, "N")

print('earth.acc = ', end='')
print(earth.acc, "m/s^2")
print('apple.acc = ', end='')
print(apple.acc, "m/s^2")
