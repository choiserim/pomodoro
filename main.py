from tkinter import *
import time
import math
from PIL import ImageTk, Image

"""
3개의 레이아웃 관리자
pack: 각각의 위젯을 논리적인 형태로 다음 위젯 옆에 배치하는 역할을 한다.
      항상 위에서 부터 배치되고 다른 위젯은 이전 것의 바로 아래에 배치된다.
      배치는 side= 를 이용하여 변경할 수 있다. 문제는 정확한 위치에 배치할 수 없다.

place: 정확한 위치 선정에 관한 것이다. 그래서 어떤 위쳇을 만들 때 x와 y값을 설정할 수 있다.
       문제는 x와 y값을 정확하게 계산하여 위치를 선정할 수 있다.

grid: 엑셀 표처럼 생각하여 행과 열을 설정하여 위젯을 배치할 수 있다.
      다른 위젯이 없을 경우는 행과 열에 어떤 값을 입력해도 첫 번째 위젯으로 인식되어 0, 0위치에 배치된다.
      그래서 항상 위에서 부터 원하는 위젯을 배치하여 사용한다.  

*pack와 grid는 같은 프로그램에서 사용할 수 없다.      
"""

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark_position = 3
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def time_reset():

    window.after_cancel(str(timer))
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def time_start():

    global reps
    global mark_position
    reps += 1
    mark_position += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=GREEN)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work Time", fg=RED)
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60

    # dynamic type
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        time_start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=300, height=400)
window.title(string="Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
# timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

# import tomato image
# highlightthickness=0 -> 경계선 없애는 방법
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

# img = ImageTk.PhotoImage(Image.open("tomato.png"))
# img_laber = Label(image=img)
# img_laber.grid(column=1, row=1)

# start button
# highlightthickness=0 -> 경계선 없애는 방법
start_button = Button(text="Start", highlightthickness=0, command=time_start)
start_button.grid(column=0, row=2)

# check mark
# check_mark = Canvas(width=15, height=15)
# check_mark.create_text(9, 10, text="✔")
# check_mark.grid(column=1, row=3)

check_mark = Label(fg=RED, bg=YELLOW)
check_mark.grid(column=1, row=3)


# reset button
# highlightthickness=0 -> 경계선 없애는 방법
reset_button = Button(text="Reset", highlightthickness=0, command=time_reset)
reset_button.grid(column=2, row=2)

window.mainloop()
