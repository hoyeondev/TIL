import turtle
import time
import tkinter as tk
import tkinter.messagebox as msgbox
from tkinter import simpledialog

'''
동작설명: 사용자의 입력값을 받아 거북이가 오름차순으로 버블정렬 여행을 떠납니다.
버블정렬을 활용한 gui 프로그램
'''

# 사용자 입력 받기
def get_user_input():
    root = tk.Tk()
    root.withdraw()
    input_str = simpledialog.askstring("Input", "정렬할 숫자를 쉼표로 구분해서 입력하세요 (예: 4,2,7,1):")
    root.destroy()

    if input_str:
        try:
            return [int(num.strip()) for num in input_str.split(',')]
        except ValueError:
            #print("숫자 형식 오류! 올바르게 입력해주세요.")
            msgbox.showerror("입력 오류", "숫자 형식 오류! 올바르게 입력해주세요.")
            return []
    return []

# 막대 그리기
def draw_bars(values):
    drawer.clear()
    total_width = len(values) * (BAR_WIDTH + BAR_SPACING) - BAR_SPACING
    start_x = -total_width / 2

    for i, val in enumerate(values):
        x = start_x + i * (BAR_WIDTH + BAR_SPACING)
        drawer.goto(x, BASE_Y)
        drawer.pendown()
        drawer.begin_fill()
        drawer.fillcolor("skyblue")
        for _ in range(2):
            drawer.forward(BAR_WIDTH)
            drawer.left(90)
            drawer.forward(val * 5)
            drawer.left(90)
        drawer.end_fill()
        drawer.penup()
        drawer.goto(x + BAR_WIDTH / 4, BASE_Y - 20)
        drawer.write(str(val), font=("Arial", 12, "normal"))

# 거북이 이동
def move_turtle_to_index(index):
    if index < 0:
        comparer.goto(-1000, -1000)
        return
    total_width = len(values) * (BAR_WIDTH + BAR_SPACING) - BAR_SPACING
    start_x = -total_width / 2
    x = start_x + index * (BAR_WIDTH + BAR_SPACING) + BAR_WIDTH / 2
    y = BASE_Y + 100
    comparer.goto(x, y)

# 메세지 출력 효과
def show_message(text, x, y):
    msg_writer.clear()
    msg_writer.goto(x, y)
    msg_writer.write(text, align="center", font=("Arial", 14, "bold"))
    time.sleep(0.8)
    msg_writer.clear()

def show_completion_message():
    msg_writer.goto(0, 150)
    msg_writer.color("blue")
    msg_writer.write("🎉 정렬 완료! 🎉", align="center", font=("Arial", 24, "bold"))

# 버블 정렬 시각화
def bubble_sort_visual(values):
    n = len(values)
    for i in range(n):
        swapped = False  # 자리 바꿈 여부 체크 변수
        for j in range(0, n - i - 1):
            move_turtle_to_index(j)
            time.sleep(0.5)
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True   # 자리 바꿈 발생
                # 메세지 표시
                msg_x = comparer.xcor()
                msg_y = comparer.ycor() + 40
                show_message("버블버블", msg_x, msg_y)
                # 그래프 그리기
                draw_bars(values)
                time.sleep(0.5)
            else:
                if swapped:
                    move_turtle_to_index(j)
                    # swapped가 False이면 거북이 이동 생략
                    # 메세지 표시
                    msg_x = comparer.xcor()
                    msg_y = comparer.ycor() + 40
                    show_message("....", msg_x, msg_y)
                
        if not swapped:  # 자리 바꿈이 없으면 정렬 완료
            break
    show_completion_message()
    move_turtle_to_index(-1)
    

# 설정
BAR_WIDTH = 40
BAR_SPACING = 10
BASE_Y = -100

screen = turtle.Screen()
screen.title("버블 정렬 시뮬레이션")
screen.bgcolor("white")
screen.setup(width=800, height=600)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

comparer = turtle.Turtle()
comparer.shape("turtle")
comparer.color("green")
comparer.penup()
comparer.speed(1)

msg_writer = turtle.Turtle()
msg_writer.hideturtle()
msg_writer.penup()
msg_writer.color("green")

# 실행
values = get_user_input()
if values:
    draw_bars(values)
    screen.update()
    time.sleep(1)
    msg_x = comparer.xcor()
    msg_y = comparer.ycor() + 40
    # 시작 메세지 출력
    show_message("버블정렬 시작!", msg_x, msg_y)
    bubble_sort_visual(values)
    screen.mainloop()
else:
    print('오류발생')
    #msgbox.showerror("입력 오류", "입력값이 없거나 잘못된 형식입니다.")



