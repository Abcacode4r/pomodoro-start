from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 24
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
Rep=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
           window.after_cancel(timer)
           canvas.itemconfig(timer_text, text="00:00")
           Title_Label.config(text="Timer")
           Check_mark.config(text="")
           global Rep
           Rep=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
def start_timer():
    global Rep
    Rep+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if Rep%8==0:
        count_down(long_break_sec)
        Title_Label.config(text="End of Session", fg="RED")
    if Rep%2==0:
        count_down(short_break_sec)
        Title_Label.config(text="Short Break", fg="PINK")

    else:
        count_down(work_sec)
        Title_Label.config(text="Work Time", fg="GREEN")
def count_down(count):
    count_sec=count%60
    count_min=math.floor(count/60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    print(count)
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(Rep/2)
        for _ in range(work_sessions):
            mark+="✓"
            Check_mark.config(text=mark)


window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg="YELLOW")
canvas=Canvas(width=210,height=230,bg="YELLOW",highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,105,image=tomato_img)
timer_text=canvas.create_text(100,130,text="0:0",fill="White",font=(FONT_NAME,34,"bold"))
canvas.grid(column=1,row=1)
Title_Label=Label(text="Timer", font=("Arial", 34, "bold"), fg="GREEN", bg="YELLOW")
Title_Label.grid(column=1, row=0)
Check_mark=Label(font=("Arial",15,"bold"),fg="GREEN",bg="YELLOW")
Check_mark.grid(column=1,row=3)
Start=Button(text="Start",highlightthickness=0,command=start_timer)
Start.grid(column=0,row=2)
Reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
Reset.grid(column=2,row=2)







window.mainloop()