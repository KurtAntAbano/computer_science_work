from tkinter import *

userForm=Tk()
userForm.title("Testing GUI")
userForm.geometry("70x200")
timerTicks=0
timings=[0,6,9,12]

def timer1():
    global timerTicks
    timerTicks+=1
    lblTimer.configure(text=timerTicks)
    setLights()
    userForm.after(400,timer1)


def setLights():
    global timerTicks
    if timerTicks>18:
        timerTicks=19
    elif timerTicks>15:
        turnRedAmber()
    elif timerTicks>12:
        turnRed()
    elif timerTicks>6:
        turnAmber()
    else:
        turnGreen()



def turnRed():
    C.itemconfig(cRed, fill=Lights[cRed])
    C.itemconfig(cAmber, fill=Lights[0])
    C.itemconfig(cGreen, fill=Lights[0])


def turnRedAmber():
    C.itemconfig(cRed, fill=Lights[cRed])
    C.itemconfig(cAmber, fill=Lights[cAmber])
    C.itemconfig(cGreen, fill=Lights[0])


def turnAmber():
    C.itemconfig(cRed, fill=Lights[0])
    C.itemconfig(cAmber, fill=Lights[cAmber])
    C.itemconfig(cGreen, fill=Lights[0])


def turnGreen():
    C.itemconfig(cRed, fill=Lights[0])
    C.itemconfig(cAmber, fill=Lights[0])
    C.itemconfig(cGreen, fill=Lights[cGreen])


def turnOff():
    C.itemconfig(cRed, fill=Lights[0])
    C.itemconfig(cAmber, fill=Lights[0])
    C.itemconfig(cGreen, fill=Lights[0])




C = Canvas(userForm, bg="grey", height=170, width=70)
#coord = 10, 50, 240, 210
Top=10
Left=10
Size=50
cRed = C.create_oval(Left,Top, Left+Size,Top+Size)
cAmber = C.create_oval(Left,Top+Size, Left+Size, Top+Size*2)
cGreen = C.create_oval(Left,Top+Size*2, Left+Size, Top+Size*3)
C.pack()
Lights={cRed:"red",cAmber:"yellow",cGreen:"green",0:"black"}
turnOff()
lblTimer=Label(userForm)
lblTimer.pack()
timer1()


userForm.mainloop()


