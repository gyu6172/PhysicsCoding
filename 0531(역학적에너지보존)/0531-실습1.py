from vpython import *

s_f = 3

Earth = sphere(pos=vec(0, 0, 0), radius=6371000*s_f, texture = textures.earth)
Moon = sphere(pos=vec(3.8e8, 0, 0), radius=1737000*s_f, make_trail=True)

G = 6.67e-11

# 물리 성질 초기화
Earth.mass = 5.972e24 #지구 질량
Moon.mass = 7.36e22 #달 질량

# 달의 초기속도 설정
vi = sqrt(G*Earth.mass/mag(Earth.pos-Moon.pos)**1)

#Moon.v = vec(0,vi*0.7,0) #타원
Moon.v = sqrt(2)*vec(0,vi,0)
#Moon.v = sqrt(3)*vec(0,vi,0) #쌍곡선

#Earth.v = vec(0,0,0)
Earth.v = -Moon.v*Moon.mass/Earth.mass

# 그래프
k_graph = gcurve(color = color.cyan)
u_graph = gcurve(color = color.green)
ku_graph = gcurve(color = color.black)

t=0
dt = 60*60

# 시뮬레이션 루프
while t < 365*24*60*60:
    rate(60)

    # 만유인력
    r = Moon.pos - Earth.pos

    Moon.f = (-G*Earth.mass*Moon.mass/mag(r)**2)*norm(r)
    # 뉴턴 제 3법칙 적용 (작용반작용)
    Earth.f = -Moon.f
    # 속도, 위치 업데이트
    Moon.v = Moon.v + Moon.f/Moon.mass*dt
    #Earth.v = Earth.v + Earth.f/Earth.mass*dt
    Moon.pos = Moon.pos + Moon.v*dt
    #Earth.pos = Earth.pos + Earth.v*dt
    # 에너지 업데이트
    k = 0.5*Moon.mass*mag(Moon.v)**2
    #운동에너지
    u = -G*Earth.mass*Moon.mass/mag(Moon.pos)
    #퍼텐셜 에너지
    # 그래프 업데이트
    k_graph.plot(t/60/60/24, k)
    u_graph.plot(t/60/60/24, u)
    ku_graph.plot(t/60/60/24, k + u)
    
    t += dt
    
    # 달과 지구의 충돌시 시뮬레이션 루프 탈출
    if mag(r) < Earth.radius+Moon.radius:
        print(t/60/60/24)
        break 
    
    
    