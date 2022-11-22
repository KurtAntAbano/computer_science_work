head = 0
next_free = -99

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

    element = input("input taxi")
    taxi[0][0] = element
    taxi[0][1] = -1
    next_free += 1
    print(taxi)

    for i in range(0, 10):
        element = input("input taxi")
        taxi[next_free][0] = element           # update element
        taxi[next_free-1][1] = next_free             # updating previous elements pointer
        taxi[next_free][1] = -1                   #updating curent elements pointer to -1 (Not linked to anything)
        next_free += 1
        print(taxi)


add_taxi()