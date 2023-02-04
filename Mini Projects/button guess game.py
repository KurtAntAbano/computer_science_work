import tkinter as tk
import random
from tkinter import messagebox

score = 0
def main():
    options = random.randint(1,3)
    if options == 1:
        layout = ["lose", "lose", "win"]
    elif options == 2:
        layout = ["lose", "win", "lose"]
    elif options == 3:
        layout = ["win", "lose", "win"]

    window = tk.Tk()
    window.title("Welcome to the door guessing game")
    window.geometry("400x200")

    welcomelabel = tk.Label(window, text ="Welcome to my door guessing game")
    welcomelabel.config(font=("Courier", 13))
    welcomelabel.grid(row = 0, column = 0, columnspan=3, sticky="W", padx = 10, pady = 10)

    helplabel = tk.Label(window, text = "Choose a door to go through \nyou have a 1/3 chance of winning the right door\n correct door = + 1 point, incorrect door = -1 point")
    helplabel.grid(row = 1, rowspan= 3, column = 2, padx=5, pady=5)


    scorelabel = tk.Label(window, text = "SCORE:\n"+ str(score))
    scorelabel.grid(row = 4, rowspan= 3, column = 2, padx=5, pady=5)


    button1 = tk.Button(window, text="Door 1", command=lambda: check(layout[0],window))
    button1.grid(row=2, column=0, padx=10, pady=10)
    button2 = tk.Button(window, text="Door 2", command=lambda: check(layout[1],window))
    button2.grid(row=3, column=0, padx=10, pady=10)
    button3 = tk.Button(window, text="Door 3", command=lambda: check(layout[2],window))
    button3.grid(row=4, column=0, padx=10, pady=10)

    window.mainloop()


def check(b, window):
    global score
    if b == "win":
        messagebox.showinfo(message=" YOU WIN\n +1 points")
        score += 1
    elif b == "lose":
        messagebox.showinfo(message=" YOU LOSE\n -1 points")
        score -= 1
    msgbox = messagebox.askquestion(title="continue...", message="would you like to continue?")
    if msgbox == "yes":
        window.destroy()
        main()
    else:
        quit()


main()
