import random

# add global variables here
guess = 0
number = 0


def prime():
    global number
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("it's not a prime number")
            else:
                print("it's a prime number")
            break


def ran():
    global guess  # declare as global
    global number
    number = random.randint(1, 20)
    prime()
    while guess != number:
        guess = int(input("Guess my number from 1 to 20"))
        if guess > number:
            print("Too big")
        elif guess < number:
            print("Too small")
        elif guess == number:
            print("Great job u did it")



def main():
    global guess
    global number
    print("Im guessing a number")
    ran()
    while guess != number:
        ran()


main()
