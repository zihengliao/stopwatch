from tkinter import *
from PIL import ImageTk, Image
import time


window = Tk()
window.geometry("800x500")
window.configure(bg = "black")
window.resizable(False,False)





total_time = 0  # this is for js
total_time_disc = 0






def pause():
    global total_time
    global current_time 
    global running
    
    running = False
    total_time = current_time
    js_button = Button(window, text = "js start", command = start)
    js_button.place(relx = 0.25, rely = 0.9)



def start():
    global total_time
    global current_time 
    global running
    
    running = True
    start_time = time.time()
    js_button.destroy()
    while running:
        end_time = time.time()
        current_time = int(end_time - start_time + total_time) # this is in seconds
        
        frame = Frame(window, width=100, height=40, bg = "yellow")
        frame.place(relx = 0.175, rely = 0.75)

        minutes = current_time // 60
        seconds = current_time % 60
        hours = minutes // 60
        minutes = minutes % 60


        js_time = Label(frame, text = f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds", font=('Lucida font',10), bg = "yellow")
        js_time.pack(pady=20)
        # js_time.pack()

        js_stop_button = Button(window, text = "js stop", command= pause)
        js_stop_button.place(relx = 0.25, rely = 0.9)

        window.update()
        time.sleep(1)



def disc_running():
    global disc_run
    global total_time_disc
    disc_run = True
    start_time = time.time()
    while disc_run:
        end_time = time.time()
        current_time = int(end_time - start_time + total_time_disc) # this is in seconds
        
        frame = Frame(window, width=100, height=40, bg = "blue")
        frame.place(relx = 0.575, rely = 0.75)

        minutes = current_time // 60
        seconds = current_time % 60
        hours = minutes // 60
        minutes = minutes % 60


        js_time = Label(frame, text = f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds", font=('Lucida font',10), bg = "blue")
        js_time.pack(pady=20)
        window.update()
        time.sleep(1)

    total_time_disc = current_time


def disc_stop():
    global disc_run

    disc_run = False






# displaying images
image = Image.open("js.png")
jsimg = image.resize((300, 300))
js_img = ImageTk.PhotoImage(jsimg)
disc_img = ImageTk.PhotoImage(Image.open("discord.png").resize((300, 300)))

label = Label(image = js_img)
label.place(relx = 0.1, rely = 0.1)
label = Label(image = disc_img)
label.place(relx = 0.5, rely = 0.1)



# js start/stop button
js_button = Button(window, text = "js start", command = start)
js_button.place(relx = 0.25, rely = 0.9)

# discord start stop button
disc_button = Button(window, text = "disc start", command = disc_running)
disc_button.place(x = 475, y = 450)
disc_button = Button(window, text = "disc stop", command = disc_stop)
disc_button.place(x = 545, y = 450)

# my goals
goal_frame = Frame(window, width = 700, height = 30, bg = "black")
goal_frame.place(x = 50, y = 10)

js_goal = Label(goal_frame, text = "8 HOURS", font = ('Arial', 20), fg = "yellow", bg = "black")
js_goal.place(relx = 0.2, rely = 0)

disc_goal = Label(goal_frame, text = "2 HOURS", font = ('Arial', 20), fg = "blue", bg = "black")
disc_goal.place(relx = 0.65, rely = 0)

window.mainloop()



