from tkinter import *
import math
import winsound
window=Tk()

'''
tick mark comes when the whole loop is completed after 25 min+short break
reps will are changing ok I want check mark after every break comes
25 min done a check mark
not 5 min break
25 min don break tick comes rep 3
'''


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():

    #timer variabe should become none calling timer window
    window.after_cancel(timer) #it will cancel and time stops there only

    #now I am initalizing to the beginnig
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    #reset checkmarks
    check_mark.config(text="")
    #reset reps
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    #reps must increase al the time whenver func is called
    reps+=1
    #attached to a button 1min=60 sec so 5 min 5:00 to 4:59 like this the timer should decrease 5 4 3 21 are min nd 00,59 are sec divind 300/60=ans as 5 min300%60=0 as the mod 245/60=4.08=4  245%60=5 as the remainder so 4:05 time must be seen
    #count_down(5*60) now in the beginnig I want 5:00 not 5:0
    #count_down(5*60)->only for the testing
    #25 min to sec
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60


    if reps%8==0:

        #if 8th rep
        count_down(long_break_sec)
        title_label.config(text="Long Break",fg=RED)
        #window.update()
        #if it's 2nd /4th/6th
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
        #window.update()
    else:
        # if its the 1/3rd/5th/7th rep it should give it works
        count_down(work_sec)
        title_label.config(text="Work Time", fg=GREEN)
        #window.update()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
'''
8th is before 8 is even
first 25 min is work 1
5 min break 2
25 min work 3
5 min break 4
25 min work 5
5 min break 6 th rep
even no is 8 long break at odd it works

5
4
3
2
1
5 to 4 it takes 1 sec time(example)
every sec countdown will decrease
import time
count=5
while True:
    time.sleep((1))
    #after 1 sec dec to 1 the count
    count-=1
    #but this is a console application programs CUI
    
click on start keep watching all the time in GUI

#after takes the variables ms and a  function 1s=1000ms last element as args-->any no of variable thing thing takes the parameter hello after 1 sec the value is printed-->but I want a looping concept
def say(thing,b):
    print(thing,b)
window.after(1000,say,"Hello",24)
 ''''''
    245/60=4-->min
    245%60=5-->sec
    print(2+"sachin")#gives type errot because python,Java(features) is a strongly typed language-->typed means int, float are typed it checks for the types very strongly never allow string+interger here count_sec is a integer but then I made string this code won't run in java
    count_sec==0:
       data type is int but I made as string it is called as dynamic typing(advantage) stronly typed but allows dynamic typing can check the variable type in pytohon again sigle digit
'''
def count_down(count):
    global timer
   #it gives decimal ans
    count_min=math.floor(count/60)
    count_sec=count%60 #it gives int ans only
    if count_sec<10:
        #dynamic typing
        count_sec=f"0{count_sec}"  #in this format I wanted 00 not only 0 even when sigle digit comes like 1 ,3 then I want 01 as a second

    #after 1 second count_down is called recursion is there passed again and again first 5 4 3 2 1 0 -1 ....stop it also exactly 1 sec
   #print(count)
    #tomato the canvas timer becomes 5 4 3 2 1
    #title_label.config(text=count) #seen in timer in text
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}") #seen in tomato
    if count>0:
        #global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer() #now timer will go automatically to work to short break I won't have to press start again and again
        #I don't want heading a timer only if short_break change timer to short_break and then to lon_break

        #when we click on start the button then only timer must inside the tomato
        marks=""
        #keep on looping 8 total so 4 check should comes 2nd time it is coming reps/2 is float stronly typed
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        check_mark.config(text=marks)

        #Play a beep sound when the countdown reaches zero
    if count==0:
        winsound.Beep(1000,1000) #Play for 1 second

# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro Technique")
window.config(padx=50,pady=50,bg="#f7f5dd")
title_label=Label(text="Timer",fg="green",font="Courier 30 bold",bg="#f7f5dd",highlightthickness=0)
title_label.grid(row=0,column=1)


#something to be put on window use canvas if I put the image directly placing 1 more  object becomes difficult -->becomes hidden painting stand 1 painging once turn the sheets I can put tomato and on top of that put anything nothing happens
canvas=Canvas(width=500,height=550,bg="#f7f5dd",highlightthickness=0)

#image must be fetched as a file photoimage-->image has something whiting around it
tomato_image=PhotoImage(file="tomato.png")
#can't directly type here image name in canvas can do in windows though
canvas.create_image(250,250,image=tomato_image)
#text on canvas-->fill is the color
timer_text=canvas.create_text(250,278,text="00:00",fill="white",font="Courier 22 bold")
canvas.grid(row=1,column=1)
# #calling the function
# count_down(5)
#grid lines are used here
#canvas.create_text(text="Timer",fill="green")


#button in put on the window because it is not touching anything
start=Button(text="Start",highlightthickness=0,font="Courier 22 bold",command=start_timer)
start.grid(row=2,column=0)
reset=Button(text="Reset",highlightthickness=0,font="Courier 22 bold",command=reset_timer)
reset.grid(row=2,column=2)

#I want 4 check marks 4 ticks are seen then it is been reset and all the tick marks are ddisappeared sir divided this into a grid
'''
0  1  2
1
2
3
I have many widgets don't place everything on the window Upon window(framework) we pout a canvas (can create n no of canvas) can view only 1 canvas at a time

link shared in whatsapp converte file to a exe file runnable file then only exe file will run just run can't see the code but run the code
'''

#checkmarks just a label
check_mark=Label(bg="#f7f5dd",font="Courier 22 bold")
check_mark.grid(row=3,column=1)








window.mainloop()