from vpython import *

# 당구공 객체 생성 함수
def initBall(p, r, mass, color):
    ball = sphere(pos=p, radius=r, color=color)
    ball.v = vec(0, 0, 0)
    ball.m = mass
    ball.f = vec(0, 0, 0)
    return ball

# 벽 객체 생성 함수
def initPlate(pos, size):
    plate = box(pos=pos, size=size, color=color.green)
    return plate

# 키보드이벤트 함수
def on_keydown(event):
    global shoot
    global gamestate
    # 좌/우 방향키 : 각도 조절
    if (event.key == "left"):
        shoot.theta += 1
    elif (event.key == "right"):
        shoot.theta -= 1
    # 상/하 방향키 : 세기 조절
    elif (event.key == "up" and shoot.power < 0.8):
        shoot.power += 0.01
    elif (event.key == "down" and shoot.power > 0):
        shoot.power -= 0.01
    # Shift키 : 공 발사
    elif (event.key == "shift"):
        gamestate['ready'] = False
        gamestate['shoot'] = True

# 공끼리의 충돌 감지 함수
def collision_ball(b1, b2, e):
    n = b1.pos - b2.pos
    n_hat = norm(n)
    dist = mag(n)
    v_relm = dot(b1.v - b2.v, n_hat)
    tot_radius = b1.radius + b2.radius
    if v_relm > 0:
        return False
    if dist > tot_radius:
        return False
    if (dist <= tot_radius):
        j = -(1+e)*v_relm
        j = j/(1/b1.m+1/b2.m)
        b1.v = b1.v + j*n_hat/b1.m
        b2.v = b2.v - j*n_hat/b2.m
        b1.v *= 0.8
        b2.v *= 0.8

        return True

#공이 벽을 맞고 튕기게 하는 함수
def collision_plate(ball, table, e):
    if -table.size.x/2 > ball.pos.x - ball.radius:
        ball.pos.x = -table.size.x/2 + ball.radius
        ball.v.x = -e*ball.v.x

    if table.size.x/2 < ball.pos.x + ball.radius:
        ball.pos.x = table.size.x/2 - ball.radius
        ball.v.x = -e*ball.v.x

    if -table.size.z/2 > ball.pos.z - ball.radius:
        ball.pos.z = -table.size.z/2 + ball.radius
        ball.v.z = -e*ball.v.z

    if table.size.z/2 < ball.pos.z + ball.radius:
        ball.pos.z = table.size.z/2 - ball.radius
        ball.v.z = -e*ball.v.z

#공이 구멍으로 들어갔는지 여부를 체크하는 함수
def collisionHole(ball, hole_pos):
    global hole_r
    if(mag(ball.pos - hole_pos) < hole_r):
        return True
    else:
        return False

#공의 위치를 업데이트 하는 함수
def updatePos(ball, dt):
    global g, uk
    ball.f = -uk*ball.m*mag(g)*norm(ball.v)
    ball.v += ball.f/ball.m*dt
    ball.pos += ball.v*dt
    if(mag(ball.v) < 0.01):
        ball.v = vec(0, 0, 0)

#공의 반지름과 질량
r = 0.0285  #2.85cm
m = 0.17    #170g

#공의 색깔 리스트
color_list = [
    color.yellow,
    color.blue,
    color.red,
    color.green,
    color.black,
    color.orange,
    color.purple,
    color.cyan,
    color.magenta,
    color.yellow,
    color.blue,
    color.red,
    color.green,
    color.orange,
    color.purple,
]

#공의 위치벡터 리스트
initpos_list = []

#공 객체 리스트
ball_list = []

#위치벡터 리스트 초기화
for i in range(5):
    for j in range(-i, i+1, 2):
        initpos_list.append(vec(r*j, 0, -sqrt(3)*i*r-0.3))

#흰 공(플레이어가 치는 공)을 공 객체 리스트에 가장 먼저 추가
ball_list.append(initBall(vec(0, 0, 0.8), r, m, color.white))

#공 객체 생성함수를 이용하여 공 객체 리스트에 공을 하나씩 추가함
for i in range(1, 16):
    ball_list.append(initBall(initpos_list[i-1], r, m, color_list[i-1]))

#테이블의 가로, 세로 길이
w = 1.27
h = 2.54
table = box(pos=vec(0, -r-0.05, 0), size=vec(w, 0.1, h), color=color.green)

#벽 객체 리스트
plate_list = []

#구멍의 반지름
hole_r = 0.07

#벽의 너비, 높이, 두께
pw = w-2*hole_r
ph = 0.1
pt = 0.001

#벽 객체 리스트에 벽들을 하나씩 추가
plate_list.append(initPlate(vec(0, 0, -h/2), vec(pw, ph, pt)))
plate_list.append(initPlate(vec(0, 0, h/2), vec(pw, ph, pt)))
plate_list.append(initPlate(vec(w/2, 0, h/4), vec(pt, ph, pw)))
plate_list.append(initPlate(vec(w/2, 0, -h/4), vec(pt, ph, pw)))
plate_list.append(initPlate(vec(-w/2, 0, h/4), vec(pt, ph, pw)))
plate_list.append(initPlate(vec(-w/2, 0, -h/4), vec(pt, ph, pw)))

#구멍의 위치 벡터를 담은 리스트
hole_list = []
hole_list.append(vec(w/2, 0, h/2))
hole_list.append(vec(w/2, 0, 0))
hole_list.append(vec(w/2, 0, -h/2))
hole_list.append(vec(-w/2, 0, h/2))
hole_list.append(vec(-w/2, 0, 0))
hole_list.append(vec(-w/2, 0, -h/2))

#흰 공의 속도를 나타내는 화살표객체
shoot = arrow(pos=ball_list[0].pos, color=color.white, shaftwidth=0.005)
shoot.power = 0.3
shoot.theta = -180
shoot.axis = vec(shoot.power*sin(radians(shoot.theta)),
                 0, shoot.power*cos(radians(shoot.theta)))

#마찰계수Uk와 중력가속도g
uk = 0.02
g = vec(0, -9.8, 0)

#게임의 현재 상태를 나타내는 딕셔너리
gamestate = {'ready': True, 'shoot': False,
             'gameover': False, 'gamelose': False, 'gamewin': False}

#키보드 이벤트 리스너 등록
scene.bind("keydown", on_keydown)

t = 0
dt = 0.001
while not gamestate['gameover']:
    rate(1/dt)

    #만약 공 리스트에 공 하나만 남아있다면(모든 공을 넣었다면)
    if (len(ball_list) == 1):
        #게임 승리, 종료
        gamestate['gameover'] = True
        gamestate['gamewin'] = True

    #게임이 'ready'상태라면
    if(gamestate['ready']):
        #카메라를 흰 공에 맞춘다.
        scene.center = ball_list[0].pos

        #흰 공을 치는 각도와 세기 업데이트
        shoot.pos = ball_list[0].pos
        shoot.visible = True
        shoot.axis = vec(shoot.power*sin(radians(shoot.theta)),
                         0, shoot.power*cos(radians(shoot.theta)))
        ball_list[0].v = 10*vec(shoot.power*sin(radians(shoot.theta)),
                                0, shoot.power*cos(radians(shoot.theta)))

    #게임이 'shoot'상태라면
    elif(gamestate['shoot']):
        #화살표를 안보이게 설정
        shoot.visible = False

        #공 리스트 안의 각 객체의 위치를 업데이트 함
        for ball in ball_list:
            updatePos(ball, dt)

        #이중for문으로 공끼리의 충돌을 검사함.
        for b1 in ball_list:
            for b2 in ball_list:
                if(b1 == b2):
                    continue
                collision_ball(b1, b2, 1)

        #공이 벽에 맞는지 검사
        for ball in ball_list:
            collision_plate(ball, table, 0.9)

        #공이 구멍에 들어갔는지 검사
        for ball in ball_list:
            for hole in hole_list:
                if(collisionHole(ball, hole)): 
                    #만약 들어간 공이 흰공이라면
                    if(ball == ball_list[0]):
                        #게임 패배, 종료
                        gamestate['gameover'] = True
                        gamestate['gamelose'] = True
                        ball.visible = False

                    #만약 들어간 공이 검은공이라면
                    elif (ball.color == color.black):
                        #게임 패배, 종료
                        gamestate['gameover'] = True
                        gamestate['gamelose'] = True
                        ball.visible = False

                    #그 외의 경우라면
                    else:
                        #공을 숨기고 리스트에서 삭제
                        ball.visible = False
                        ball_list.remove(ball)

        #공이 모두 멈추었는지 확인하는 변수
        stop = True
        for ball in ball_list:
            if(mag(ball.v) > 0):
                stop = False

        #공이 모두 멈추었다면
        if stop:
            #게임의 현재 상태 업데이트
            gamestate['ready'] = True
            gamestate['shoot'] = False

    t += dt

#게임이 종료된 후
gameover_text = label(pos=ball_list[0].pos, height=30)

#게임을 패배했다면
if(gamestate['gamelose']):
    #"Game Over"텍스트를 띄운다.
    gameover_text.text = "Game Over!"

#게임을 승리했다면
elif(gamestate['gamewin']):
    #"You Win"텍스트를 띄운다.
    gameover_text.text = "You Win!"
