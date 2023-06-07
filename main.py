from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = ""


def reset_timer():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    check_marks.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="0:00")
    start_button.config(state="normal")
    reset_button.config(state="disabled")


def handle_checkmarks():
    global reps
    work_sessions = math.floor(reps / 2)
    marks = ""

    for _ in range(0, work_sessions):
        marks += CHECKMARK

    check_marks.config(text=marks)


def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")
    reset_button.config(state="normal")

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Working", fg=GREEN)
        count_down(work_sec)
        handle_checkmarks()


def count_down(count):
    global timer
    minute = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 42), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, state="disabled")
reset_button.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 22), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
