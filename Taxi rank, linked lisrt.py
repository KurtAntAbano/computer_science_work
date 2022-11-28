head = 0
next_free = 0  # -99 in this case = 0 (it is empty)

taxi = [["", -99],
        ["", -99],
        ["", -99],
        ["", -99],
        ["", -99],
        ["", -99],
        ["", -99],
        ["", -99],
        ["", -99],
        ["", -99]]


def add_taxi():
    global head
    global next_free
    global taxi

    amount = int(input("How many taxis would you like to add"))

    element = input("input taxi")
    taxi[head][0] = element
    taxi[head][1] = -1
    next_free += 1
    print(taxi)

    for i in range(0, amount - 1):
        element = input("input taxi")
        taxi[next_free][0] = element  # update element
        taxi[next_free - 1][1] = next_free  # updating previous elements pointer
        taxi[next_free][1] = -1  # updating curent elements pointer to -1 (Not linked to anything)
        next_free += 1  # updating next_free pointer
        print(taxi)


def swap_taxi():
    global driver2_index, driver1_index
    driver1 = input("Which driver are you?")
    driver2 = input("which driver would you like to switch ranks with?")

    for i in range(0,10):
        if driver1 == taxi[i][0]:
            driver1_index = i

        if driver2 == taxi[i][0]:
            driver2_index = i

    temp = taxi[driver1_index][1]
    taxi[driver1_index][1] = taxi[driver2_index][1]
    taxi[driver2_index][1] = temp
    print(taxi)



add_taxi()

swap_taxi()
