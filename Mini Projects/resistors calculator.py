import tkinter as tk
#window = tk.Tk()

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


def enterColours():
    print("------------------  Entering Resistors Colours -------------")
    global entColours
    global bands
    bands = 5
    entColours = []  # list for the five entered colours (blank)
    n = 1
    while len(entColours) < 5:
        col = input("Please enter colour of the band " + str(n) + "  ")
        if col in colours:  # validation using list
            entColours.append(col)
            n += 1
        else:
            print()
            print(" there is no such colour ... please try again  ")
            print()


def resistor():
    print("---------- calculating the values wait ...")
    print()
    value = ""
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


createDict()
enterColours()

print()

print(" You have entered ")

print(entColours)

print()

print("which is equivelant to  ")

print(resistor())





