from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
current_rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_time():
    global current_rep
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    current_rep = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global current_rep
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    current_rep += 1

    if current_rep % 8 == 0:
        title_label.config(text="Break", fg=GREEN)
        count_down(long_break_sec)
    elif current_rep % 2 == 1:
        title_label.config(text="Work!", fg=RED)
        count_down(work_sec)
    else:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        reps = math.floor(current_rep / 2)
        for _ in range(reps):
            mark += "✓"
        checkmarks_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Countdown")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT_NAME, 45))
title_label.grid(row=0, column=1)

checkmarks_label = Label(fg=GREEN, bg=YELLOW,
                         font=(FONT_NAME, 30))
checkmarks_label.grid(row=3, column=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons

start_button = Button(text="Start", highlightthickness=0,
                      highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0,
                      highlightbackground=YELLOW, command=reset_time)
reset_button.grid(row=2, column=2)


window.mainloop()
