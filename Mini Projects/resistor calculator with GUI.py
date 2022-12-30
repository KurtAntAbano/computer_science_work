import tkinter as tk

def createDict():
    # declaring all lists and dictionaries are global
    global colourDict
    global colours
    global multDict
    global tolDict
    # declaring tolerance dictionary
    tolDict = {"Black": "", "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
               "Green": 0.5, "Blue": 0.25, "Violet": 0.1, "Grey": 0.05,
               "White": "", "Gold": 5, "Silver": 10, "No band": 20}

    # declaring colur bands 1 , 2 and 3 dictionary
    colourDict = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
                  "Green": 5, "Blue": 6, "Violet": 7, "Grey": 8, "White": 9,
                  "Gold": 0, "Silver": 0, "No Band": 0}

    colours = list(colourDict)
    # generating multiplier dictionary from colour bands dictionary
    multDict = {"Black": 1, "Brown": 10, "Red": 100, "Orange": 1000, "Yellow": 10000,
                "Green": 100000, "Blue": 1000000, "Violet": 10000000, "Grey": 100000000,
                "White": 1000000000, "Gold": 0.1, "Silver": 0.01, "No Band": 1}
    i = 0
    for value in colours:
        multDict[value] = 10 ** i
        i += 1
    multDict["Gold"] = 0.1  # adding more keys and values to the dictionary
    multDict["Silver"] = 0.01  # adding more keys and values to the dictionary

def colour_append(colour, entColours,window):
    global n
    entColours.append(colour)
    print(f"Band {n+1} is {colour}")
    if n == 4:
        window.destroy()
    else:
        n += 1

def again():
    continue_win = tk.Tk()
    button1 = tk.Button(continue_win, text="i would like to continue", command= lambda:[continue_win.destroy(),main()])
    button1.pack()
    button2 = tk.Button(continue_win, text="i would like to leave", command=exit)
    button2.pack()

    continue_win.mainloop()

def enterColours():
    global entColours
    global n
    window = tk.Tk()
    entColours = []
    n = 0

    print("PLEASE ENTER THE CCOLOUR OF THE BANDS UP TO 5\n")
    b = tk.Button(window, text="Black", command=lambda: colour_append("Black", entColours,window))
    b.pack()
    b = tk.Button(window, text="Brown", command=lambda: colour_append("Brown", entColours, window))
    b.pack()
    b = tk.Button(window, text="Red", command=lambda: colour_append("Red", entColours, window))
    b.pack()
    b = tk.Button(window, text="Orange", command=lambda: colour_append("Orange", entColours, window))
    b.pack()
    b = tk.Button(window, text="Yellow", command=lambda: colour_append("Yellow", entColours, window))
    b.pack()
    b = tk.Button(window, text="Green", command=lambda: colour_append("Green", entColours, window))
    b.pack()
    b = tk.Button(window, text="Blue", command=lambda: colour_append("Blue", entColours,window))
    b.pack()
    b = tk.Button(window, text="Violet", command=lambda: colour_append("Violet", entColours, window))
    b.pack()
    b = tk.Button(window, text="Grey", command=lambda: colour_append("Grey", entColours, window))
    b.pack()
    b = tk.Button(window, text="White", command=lambda: colour_append("White", entColours, window))
    b.pack()
    b = tk.Button(window, text="Gold", command=lambda: colour_append("Gold", entColours, window))
    b.pack()
    b = tk.Button(window, text="Silver", command=lambda: colour_append("Silver", entColours, window))
    b.pack()
    b = tk.Button(window, text="No Band", command=lambda: colour_append("No Band", entColours, window))
    b.pack()

    window.mainloop()
    print("list of bands:", entColours)



def resistor(entColours):
    global multiplier, tolerance
    print("---------- calculating the values wait ...")
    print()
    value = ""
    bands = 5
    for i in range(0, bands):
        if i < 3:
            #checks first 3 bands
            bandValue = str(colourDict[entColours[i]])
            value += bandValue
        if i == 3:
            #checks multiplier
            multiplier = multDict[entColours[i]]
        if i == 4:
            #checks tolerence
            tolerance = tolDict[entColours[i]]

    ResistorValue = int(value) * multiplier
    finalValue = convert(ResistorValue, tolerance)
    return finalValue


def convert(R, t):
    print("----------- converting values to K, M and G ------")
    print()
    if R >= 1000 and R < 1000000:
        R = str(R / 1000) + "K"
    elif R >= 1000000 and R < 1000000000:
        R = str(R / 1000000) + "M"
    elif R >= 1000000000:
        R = str(R / 1000000000) + "G"
    s = str(R) + " Ohms" + " +/-" + str(t) + "%"
    return s

def main():

    createDict()
    enterColours()

    print()

    print(" You have entered ")

    print(entColours)

    print()

    print("which is equivelant to  ")


    print(resistor(entColours))
    again()

main()





