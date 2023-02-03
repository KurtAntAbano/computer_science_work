from tkinter import *
#this allows the program to access tkinter
from tkinter import *
def CreateGUI():

    form = Tk()
    form.title("Welcome to BMI calculator")
    form.geometry("500x200")

    welcomelabel = Label(form, text ="Welcome to my BMI calculator")
    welcomelabel.config(font=("Courier", 18))
    welcomelabel.grid(row = 0, column = 0, columnspan=3, sticky="W", padx = 10, pady = 10)

    weightlabel = Label(form, text = "Weight in Kg")
    weightlabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    heightlabel = Label(form, text = "Height in Meters")
    heightlabel.grid(row=2, column = 0, padx=10, pady=10, sticky = "W")

    helplabel = Label(form, text = "enter height in m and \nweight in kg")
    helplabel.grid(row = 1, rowspan= 2, column = 2, padx=10, pady=10)

    weightentry = Entry(form, width = 30)
    weightentry.grid(row=1, column=1, padx=10, pady=10, sticky="E")

    heightentry = Entry(form, width = 30)
    heightentry.grid(row= 2, column = 1, padx = 10, pady = 10, sticky = "E")

    exitbutton = Button(form, text = "EXIT", width = 12, command = quit)
    exitbutton.grid(row=3, column=0, padx=10, pady=10)

    clearbutton = Button(form, text="Clear", width=12)
    clearbutton.grid(row=3, column=1, padx=10, pady=10)

    calcbutton = Button(form, text = "Calculate", width = 12)
    calcbutton.grid(row = 3, column = 2, padx = 10, pady =10)


def calculate():
    weight = weightentry.get()

    form.mainloop()

CreateGUI()
