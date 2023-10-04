head = 0
next_free = 0  # -99 in this case = 0 (it is empty)

cities = [["London", 1],
          ["Oxford", 2],
          ["Birmingham", 3],
          ["Manchester", "null"],
          ["", -99],
          ["", -99],
          ["", -99],
          ["", -99],
          ["", -99],
          ["", -99]]


def add_city():
    global head
    global next_free
    global cities

    amount = int(input("How many cities would you like to add"))

    element = input("input taxi")
    cities[head][0] = element
    cities[head][1] = -1
    next_free += 1
    print(cities)

    for i in range(0, amount - 1):
        element = input("input city")
        cities[next_free][0] = element  # update element
        cities[next_free - 1][1] = next_free  # updating previous elements pointer
        cities[next_free][1] = "null"  # updating curent elements pointer to -1 (Not linked to anything)
        next_free += 1  # updating next_free pointer
        print(cities)


def swap_city():
    global city2_index, city1_index
    city1 = input("Which driver are you?")
    city2 = input("which driver would you like to switch ranks with?")

    for i in range(0, 10):
        if city1 == cities[i][0]:
            city1_index = i

        if city2 == cities[i][0]:
            city2_index = i

    temp = cities[city1_index][1]
    cities[city1_index][1] = cities[city2_index][1]
    cities[city2_index][1] = temp
    print(cities)


def del_city_head():
    is_leaving = input("is the head taxi leaving? y/n")
    if is_leaving == "y":
        cities[0] = cities[1]
    print(cities)

def del_city(city):
    for i in range(0, 10):
        if cities[i][0] == city:

            if cities[i][1] == head:
                cities[i+1][1] = head

            else:
                cities[i-1][1] += 1




add_city()

swap_city()

del_city_head()
