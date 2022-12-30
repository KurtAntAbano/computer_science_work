import tkinter as tk
import random

def check(b,window):
    if b == "win":
        print("u win")
    elif b == "lose":
        print("u lose")
    window.destroy()


def again():
    continue_win = tk.Tk()
    button1 = tk.Button(continue_win, text="i would like to continue", command= lambda:[continue_win.destroy(),main()])
    button1.pack()
    button2 = tk.Button(continue_win, text="i would like to leave", command=exit)
    button2.pack()

    continue_win.mainloop()


def main():
    options = random.randint(1,3)
    if options == 1:
        layout = ["lose", "lose", "win"]
    elif options == 2:
        layout = ["lose", "win", "lose"]
    elif options == 3:
        layout = ["win", "lose", "win"]

    window = tk.Tk()

    button1 = tk.Button(window, text="Door 1", command=lambda: check(layout[0],window))
    button1.pack()
    button2 = tk.Button(window, text="Door 2", command=lambda: check(layout[1],window))
    button2.pack()
    button3 = tk.Button(window, text="Door 3", command=lambda: check(layout[2],window))
    button3.pack()

    window.mainloop()
    again()


main()
