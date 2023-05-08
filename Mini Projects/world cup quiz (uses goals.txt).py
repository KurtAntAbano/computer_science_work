import random

def country_goal_list():
    countries = []

    file = open("goals.txt", "r")

    for line in file:
        data = line.split(";")
        country = data[1]
        if country not in countries:
            countries.append(country)

    file.close()
    main(countries)

def how_many_goals(country):
    file = open("goals.txt", "r")
    count = 0

    for line in file:
        data = line.split(";")
        if data[1] == country:
            count += int(data[2])

    return count



def main(countries):
    randomCountry1 = random.choice(countries)
    randomCountry2 = random.choice(countries)

    whichCountry = int(input(f"Which country do u think scored more goals? {randomCountry1} or {randomCountry2} (1 or 2)"))
    Country1_goals = how_many_goals(randomCountry1)
    Country2_goals = how_many_goals(randomCountry2)

    if Country1_goals > Country2_goals:
        answer = 1
    else:
        answer = 2

    if whichCountry == answer:
        print("\nWell done, you are correct")
    else:
        print("\nsorry ur wrong")

    print(f"\n{randomCountry1} scored {Country1_goals}, {randomCountry2} scored {Country2_goals}")

country_goal_list()

