import tkinter as tk
import random

options = ["safe", "wrong"]


def check():
    check = random.choice(options)
    if check == "safe":
        print("safe")
    if check == "wrong":
        print("you die")


window = tk.Tk()

button1 = tk.Button(window, text = "1",command = check)
button1.pack()
button2 = tk.Button(window, text = "2",command = check)
button2.pack()
button3 = tk.Button(window, text = "3",command = check)
button3.pack()

window.mainloop()