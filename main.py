from tkinter import *

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
button_clicked = False
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global button_clicked, reps
    button_clicked = False
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def on_button_click():
    global button_clicked
    if not button_clicked:
        start_timer()
        button_clicked = True


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps < 8:
        if reps % 2 == 0:
            count_down(work_sec)
            timer_label.config(fg=GREEN, text="Work")
        elif reps == 7:
            count_down(long_break_sec)
            timer_label.config(fg=RED, text="Break")
        elif reps % 2 != 0:
            count_down(short_break_sec)
            timer_label.config(fg=PINK, text="Break")
        reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = "{:02d}".format(int(count / 60))
    count_sec = "{:02d}".format(count % 60)
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        window.after(1000, start_timer)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        if reps % 2 != 0:
            checks = ""
            for n in range(int((reps + 1) / 2)):
                checks += "✔"
            checkmark_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=on_button_click, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
checkmark_label.grid(row=3, column=1)

window.mainloop()
