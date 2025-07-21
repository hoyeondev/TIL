import turtle
import time
import random

'''
🐍 스네이크 게임
1. 먹이를 먹으면 몸이 길어지며 점수를 얻는다.
2. 벽이나 길어진 몸에 부딪히면 게임 종료
'''
# 기본 설정
delay = 0.1
score = 0

# 화면 설정
win = turtle.Screen()
win.title("🐍 스네이크 게임")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)


# 게임 시작 메시지
start_msg = turtle.Turtle()
start_msg.hideturtle()
start_msg.color("white")
start_msg.penup()
start_msg.goto(0, 0)
start_msg.write("게임 Start!", align="center", font=("Arial", 28, "bold"))
win.update()
time.sleep(2)
start_msg.clear()

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake body segments
segments = []

# 먹이 만들기
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 점수판
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# 이동 함수
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

# 이동 처리
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 키 입력(키보드)
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")


# 게임 루프
while True:
    
    # 화면 갱신
    win.update()

    # 벽에 부딪힘
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        
        # 메시지 출력용 거북이
        message = turtle.Turtle()
        message.hideturtle()
        message.color("white")
        message.penup()
        message.goto(0, 0)
        message.write(f"죽었다!\n최종 점수: {score}", align="center", font=("Arial", 24, "bold"))
        # 화면 갱신
        win.update()
        
        # 초기화
        head.goto(0, 0)
        head.direction = "stop"
        #print('stop')
        for seg in segments:
            seg.goto(1000, 1000)
        segments.clear()
        score = 0
        score_display.clear()
        score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        
        # 잠깐 메시지 보여주고 지우기
        time.sleep(2)
        message.clear()

    # 먹이와 충돌
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # 몸통 추가
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()
        segments.append(new_segment)

        # 점수 추가
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # 몸통 움직이기
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # 자기 몸에 부딪힘
    for segment in segments:
        
        if segment.distance(head) < 20:
            time.sleep(1)
            
            # 메시지 출력용 거북이
            message = turtle.Turtle()
            message.hideturtle()
            message.color("white")
            message.penup()
            message.goto(0, 0)
            message.write(f"죽었다!\n최종 점수: {score}", align="center", font=("Arial", 24, "bold"))
            # 화면 갱신
            win.update()
            message.clear()
            
            head.goto(0, 0)
            head.direction = "stop"
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()
            score = 0
            score_display.clear()
            score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
