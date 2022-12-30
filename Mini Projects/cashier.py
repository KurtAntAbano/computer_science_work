coinsPence = [200, 100, 50, 20, 10, 5, 2, 1]
menu = {"Egg salad": 463, "Ham salad": 425, "Cheese sandwich": 450, "Ham sandwich": 375, "Egg sandwich": 475,
        "Humous and salad in pitta bread": 405, "Falafel in pitta bread": 399, "Chicken kebab in pitta bread": 415,
        "Cheese baguette": 250, "Samosa": 100}

funds = 500
coins = []
change = 0

def which_penny():
    global change
    global coins

    for i in range(0, len(coinsPence)):
        change = change - coinsPence[i]
        if change >= 0:
            coins.append(coinsPence[i])
        elif change < 0:
            change += coinsPence[i]
    if change != 0:
        which_penny()


def how_much_change(item):
    global change
    cost = menu[item]
    change = funds - cost
    if change < 0:
        print("you do not have enough money")
        exit()
    else:
        print(f"your change is {change}")
        which_penny()
        print(f"coins you will need:{coins}")


def main():
    print("you have £5.00")
    for keys in menu.keys():
        print(keys)
    item = input("choose from the menu:")
    how_much_change(item)


main()