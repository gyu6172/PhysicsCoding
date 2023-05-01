from vpython import *

ground = box(pos=vec(0, 0, 0), size=vec(50, 1, 5), color=color.green)

rain = sphere(pos=vec(0, 150, 0), radius=1)
rain.v = vec(0, 0, 0)
rain.m = 5e-7

rain.f = vec(0, 0, 0)

g = vec(0, -9.8, 0)  # m/s^2

rainPos = graph(title='rain Velocity', xtitle='t', ytitle='Velocity')
raingp = gcurve(color=color.red, graph=rainPos)

t = 0
dt = 0.001

while(rain.pos.y > ground.pos.y):
    rate(1/dt)

    # F = mg = kv 일때의 k값이 공기저항계수가 된다.
    # m = 5e-7, g = 9.8m/s^2, v = 20m/s이므로
    # k = mg/v
    k = (rain.m*mag(g))/20

    rain.f = (g*rain.m)+(k*-rain.v)

    rain.v += (rain.f/rain.m)*dt
    rain.pos += rain.v*dt

    raingp.plot(pos=(t, abs(rain.v.y)))

    t += dt
