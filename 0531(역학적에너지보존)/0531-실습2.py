from vpython import *

PI =  3.1415926535897932

R = 6371000
sf=10000
Earth = sphere(pos=vec(0, 0, 0), radius=R, texture = textures.earth)
ship = sphere(pos=vec(R, 0, 0), radius=5*sf, make_trail=True)

G = 6.67e-11

# 물리 성질 초기화
Earth.mass = 5.972e24 #지구 질량
ship.mass = 15000

#vi = sqrt(G*Earth.mass/R)
#vi = sqrt(1.5*G*Earth.mass/R)
vi = sqrt(2*G*Earth.mass/R)

theta = PI/4

#ship.v = vec(vi,0,0)
ship.v = vec(vi*cos(theta), vi*sin(theta), 0)

t = 0
dt = 60

v_graph = gcurve(color=color.blue)

while True:
    rate(60)
    
    r = Earth.pos - ship.pos
    
    ship.f = G*Earth.mass*ship.mass/mag(r)**2*norm(r)
    
    ship.v += (ship.f/ship.mass)*dt
    
    ship.pos += ship.v*dt
    
    v_graph.plot(pos=(t/3600,mag(ship.v)))
    
    if(mag(ship.pos - Earth.pos) < R):
        break;
    
    t+=dt
    
    
    
    