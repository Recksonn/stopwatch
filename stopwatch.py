import tkinter as tk

running = False
minutes, seconds, miliseconds = 0, 0, 0


def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    minutes, seconds, miliseconds = 0, 0, 0
    stopwatch_label.config(text='00:00:00')

def update():
    global minutes, seconds, miliseconds
    miliseconds += 1
    if miliseconds == 100:
        seconds += 1
        miliseconds = 0
    if seconds == 60:
        minutes += 1
        seconds = 0
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    miliseconds_string = f"{miliseconds}" if miliseconds > 9 else f"0{miliseconds}"
    stopwatch_label.config(text=minutes_string + ':' + seconds_string + ":" + miliseconds_string)

    global update_time
    update_time = stopwatch_label.after(10, update)


root = tk.Tk()
root.geometry('600x300')
root.title('Stopwatch')
root.config(bg="#00BFFF")

label_my = tk.Label(root, text="by Reckson", font=("Arial", "10"), bg="#00BFFF")

stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80), bg="#00BFFF",)
stopwatch_label.pack()

start_button = tk.Button(text='start', height=2, width=10, font=('Arial', 20), bg="#9370DB", command=start)
start_button.place(y=175, x=30)
pause_button = tk.Button(text='pause', height=2, width=10, font=('Arial', 20), bg="#9370DB", command=pause)
pause_button.place(y=175, x=210)
reset_button = tk.Button(text='reset', height=2, width=10, font=('Arial', 20), bg="#9370DB", command=reset)
reset_button.place(y=175, x=390)
label_my.place(y=270, x=520)



root.mainloop()