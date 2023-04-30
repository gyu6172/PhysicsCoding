from vpython import *

elev = box(pos=vec(0, 0, 0), size=vec(2, 3, 2))

elev.v = vec(0, 0, 0)
elev.a = vec(0, 0, 0)

motion_graph = graph(title='graph', xtitle='t')
atgurve = gcurve(color=color.red, graph=motion_graph)
vtgurve = gcurve(color=color.blue, graph=motion_graph)
xtgurve = gcurve(color=color.green, graph=motion_graph)

t = 0
dt = 0.01

while(t <= 10):
    rate(1/dt)
    if(1 <= t and t <= 2):
        elev.a = vec(0, 2, 0)
    elif(2 < t and t <= 5):
        elev.a = vec(0, 0, 0)
    elif(5 < t and t <= 6):
        elev.a = vec(0, -2, 0)
    elif(6 < t and t <= 7):
        elev.a = vec(0, 0, 0)
    elif(7 < t and t <= 8):
        elev.a = vec(0, -2, 0)
    elif(8 < t and t <= 9):
        elev.a = vec(0, 0, 0)
    elif(9 < t and t <= 10):
        elev.a = vec(0, 2, 0)

    atgurve.plot(pos=(t, elev.a.y))
    vtgurve.plot(pos=(t, elev.v.y))
    xtgurve.plot(pos=(t, elev.pos.y))

    elev.pos += elev.v*dt
    elev.v += elev.a*dt

    t += dt
    print(t)


print('elev=', elev.pos)
