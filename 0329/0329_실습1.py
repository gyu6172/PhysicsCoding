from vpython import *


def r(t):
    return vec(cos(pi*t), sin(pi*t), 0)


def v(t):
    return vec(-pi*sin(pi*t), pi*cos(pi*t), 0)


def a(t):
    return vec(-pi**2*cos(pi*t), -pi**2*sin(pi*t), 0)


t = 0.5

print('[수식으로 구한 결과]')
print('r(0.5)=', r(t))
print('v(0.5)=', v(t))
print('a(0.5)=', a(t))
print('[코딩으로 구한 결과]')

dt = 0.00000000001
v = (r(t+dt)-r(t))/dt
print('v(0.5)=', v)
