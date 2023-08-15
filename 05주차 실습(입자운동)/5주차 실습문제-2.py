from vpython import *

# 공, 바닥 만들기
ball = sphere(radius=0.2)
ground = box(pos=vec(0, 0, 0), size=vec(15, -0.01, 5))

# 자취 그리기
attach_trail(ball, type='points', pps=5)

thetaList = [30, 35, 40, 45, 50, 55, 60]
for theta in thetaList:

    # 물리 성질 초기화
    ball.pos = vec(-2, 0, 0)  # 공의 초기 위치 ##m
    ball.v = vec(2*cos(radians(theta)), 2 *
                 sin(radians(theta)), 0)  # 공의 초기 속도 ##m/s
    ball.a = vec(0, -0.35, 0)  # 공의 가속도 ##m/s**2

    x1 = ball.pos.x

    # 시간 설정
    t = 0  # s
    dt = 0.01  # s
    # 화살표 부착
    attach_arrow(ball, "v", shaftwidth=0.1, color=color.green)
    attach_arrow(ball, "a", shaftwidth=0.05, color=color.red)

    # 시뮬레이션 루프 (공이 바닥에 닿을 때까지)
    while ball.pos.y >= ground.pos.y:
        rate(1/dt)
        # 속도, 위치 업데이트
        ball.v = ball.v + ball.a*dt
        ball.pos = ball.pos + ball.v*dt
        # 시간 업데이트
        t = t + dt

    x2 = ball.pos.x

    print("{0}도 일때의 이동거리 : {1}".format(theta, x2-x1))
