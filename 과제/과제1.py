from vpython import *
import random as rand

# 키 입력 이벤트 구현


def on_keydown(event):
    global airplane
    if (event.key == "left" and airplane.pos.x > -9):
        airplane.pos.x -= 0.5
    elif (event.key == "right" and airplane.pos.x < 9):
        airplane.pos.x += 0.5
    elif (event.key == "up" and airplane.pos.y < 9):
        airplane.pos.y += 0.5
    elif (event.key == "down" and airplane.pos.y > -9):
        airplane.pos.y -= 0.5


# 총알 객체 리스트
bulletList = list()

# 총알 추가
for i in range(7):
    bullet = sphere(pos=vec(rand.uniform(-9, 9), 9, 0),
                    radius=0.5, color=color.red)
    bullet.v = vec(0, rand.uniform(-20, -10), 0)
    bulletList.append(bullet)

# 비행기 추가
airplane = box(pos=vec(0, -8, 0), size=vec(1, 1, 1), color=color.green)

# 게임오버 텍스트 추가
gameoverText = label(color=color.red, height=30, box=False, visible=False)

# 시간 텍스트 추가
timeText = label(pos=vec(-9, 9, 0), color=color.white)

# 무대 설정
scene.range = 10
scene.title = "Dodge Game"
scene.bind("keydown", on_keydown)
scene = canvas(pos=vec(0, 0, 0), width=800, height=600)

# 현재시간, 시간 간격, 게임 종료조건 업데이트
t = 0
dt = 0.01
gameover = False

# 게임오버가 아닌 동안
while(not gameover):
    # 1초에 100번 실행
    rate(1/dt)

    for bullet in bulletList:
        # 총알 리스트에 있는 총알 객체의 위치 업데이트
        bullet.pos += bullet.v*dt

        # 만약 총알의 y좌표가 -9보다 작다면 무대를 벗어난 것임.
        if(bullet.pos.y < -9):
            # 그 총알의 y좌표를 9로 설정
            bullet.pos.y = 9

            # x좌표는 -9와 9사이의 랜덤 실수로 설정
            bullet.pos.x = rand.uniform(-9, 9)

            # 총알이 떨어지는 속도는 -20과 -10 사이의 랜덤 실수로 설정
            bullet.v = vec(0, rand.uniform(-20, -10), 0)

        # 만약 총알과 비행기사이의 거리가 1보다 작거나 같다면 서로 충돌했다는 뜻
        if(mag(bullet.pos - airplane.pos) <= 1):
            # 게임오버
            gameover = True

            # 게임 오버 텍스트 보이게 함
            gameoverText.visible = True
            gameoverText.text = "Game Over!"
            continue
    timeText.text = "{:.2f}".format(t)

    # 시간 업데이트
    t += dt
