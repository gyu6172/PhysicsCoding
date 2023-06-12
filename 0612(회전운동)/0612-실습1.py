from vpython import *

door = box(pos=vec(0,0,0), size=vec(0.8, 2, 0.1))
door.m = 40

handle = sphere(pos=vec(0.35, 0, 0), radius=0.06, color=color.red)

t = 0
dt = 0.01

tmp = arrow(pos=vec(-0.4, -1, 0), axis=vec(0, 2, 0), shaftwidth=0.02, color=color.blue)

door.w = vec(0,0,0)

r = 0.75
F = vec(0,0,-10) #N
T = r*F

#1번문제 : 문의 회전축을 기준으로 문의 회전관성을 계산하여라.
#문의 질량중심의 회전 관성(Icom) = (1/12)*M*L^2
#문의 회전축 중심의 회전 관성(I) : I = Icom + M*h^2 
#                                   = Icom + M*(L/2)^2 
#                                   = (1/3)*M*L^2 
#                                   = (1/3)*40*(0.8)^2 = 8.5333...

#2번문제 : 손잡이에 10N, 문이 90도 도는 시간은?
# T = I*a, a = T/I, T = r*F이므로,
# T = (0.75)*10 = 7.5 (N/m)
# 따라서, a = 7.5/8.5333... = 0.8789...
# theta2 = w0*dt + (1/2)*a*dt^2. theta2 = pi/2, a=0.8789, w0 = 0이므로,
# dt = sqrt(pi/a) = 1.89초이다.

I = (1/3)*door.m*(door.size.x)**2
door.alpha = T/I

rst = vec(1,0,0)
theta2 = handle.pos - door.pos

while True:
    rate(1/dt)

    door.w += door.alpha*dt
    
    dtheta = mag(door.w)*dt
    door.rotate(angle = dtheta, axis = tmp.axis, origin = tmp.pos)
    handle.rotate(angle = dtheta, axis = tmp.axis, origin = tmp.pos)

    theta2 = handle.pos - door.pos

    if(diff_angle(rst, theta2) > pi/2):
        break

    t += dt

print('사이각 :',diff_angle(rst, theta2)*180/pi)
print('문의 회전 관성 :',I)
print('각가속도 :',door.alpha)
print('걸린 시간 :',t)