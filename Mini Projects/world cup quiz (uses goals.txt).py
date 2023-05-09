import random
from tkinter import *

from future.moves.tkinter import messagebox


def country_goal_list():
    countries = []

    file = open("goals.txt", "r")

    for line in file:
        data = line.split(";")
        country = data[1]
        if country not in countries:
            countries.append(country)

    file.close()
    mainMenuGUI(countries)


def how_many_goals(country):
    file = open("goals.txt", "r")
    count = 0

    for line in file:
        data = line.split(";")
        if data[1] == country:
            count += int(data[2])

    file.close()

    return count


def mainMenuGUI(countries):
    # code for the main menu
    # from this window, I can go to log in or signin or exit

    randomCountry1 = random.choice(countries)
    randomCountry2 = random.choice(countries)

    win1 = Tk()
    win1.title("Welcome")
    win1.geometry("400x180")

    titleLabel = Label(win1, text=f"Which country do u think scored more goals? {randomCountry1} or {randomCountry2}")
    titleLabel.grid(row=0, column=0, columnspan=3, sticky="SNEW", pady=10, padx=10)

    exitButton = Button(win1, text="Exit", width=12, command=quit)
    exitButton.grid(row=1, column=0, padx=10, pady=30)

    bt_country1 = Button(win1, text=f"{randomCountry1}", width=12,
                         command=lambda: has_won(win1, randomCountry1, randomCountry1, randomCountry2))
    bt_country1.grid(row=1, column=1, padx=10, pady=10)

    bt_country1 = Button(win1, text=f"{randomCountry2}", width=12,
                         command=lambda: has_won(win1, randomCountry2, randomCountry1, randomCountry2))
    bt_country1.grid(row=1, column=2, padx=10, pady=10)

    mainloop()


def has_won(w, country, randomCountry1, randomCountry2):
    w.destroy()

    Country1_goals = how_many_goals(randomCountry1)
    Country2_goals = how_many_goals(randomCountry2)

    if Country1_goals > Country2_goals:
        answer = 1
    else:
        answer = 2

    if country == answer:
        messagebox.showinfo(title="Success", message=(f"U ARE CORRECT!\n{randomCountry1} scored {Country1_goals},"
                                                      f" {randomCountry2} scored {Country2_goals}"))
    else:
        messagebox.showinfo(title="ERROR", message=(f"U ARE WRONG!\n{randomCountry1} scored {Country1_goals},"
                                                    f" {randomCountry2} scored {Country2_goals}"))
    country_goal_list()


country_goal_list()
