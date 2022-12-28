import tkinter as tk
import random


options = random.randint(1,3)
if options == 1:
    layout = ["lose", "lose", "win"]
elif options == 2:
    layout = ["lose", "win", "lose"]
elif options == 3:
    layout = ["win", "lose", "win"]


def check(b):
    if b == "win":
        print("u win")
    elif b == "lose":
        print("u lose")


window = tk.Tk()

button1 = tk.Button(window, text = "1",command = lambda:check(layout[0]))
button1.pack()
button2 = tk.Button(window, text = "2",command = lambda: check(layout[1]))
button2.pack()
button3 = tk.Button(window, text = "3",command = lambda: check(layout[2]))
button3.pack()

window.mainloop()