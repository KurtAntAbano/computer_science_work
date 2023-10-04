import random

# add global variables here
guess = 0
number = 0
primenum = 0

def prime():
    global number
    global primenum
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("it's not a prime number")
            else:
                primenum == 1
                print("it's a prime number")
                return primenum
            break


def ran():
    global guess  # declare as global
    global number
    global primenum
    number = random.randint(1, 20)
    prime()
    if primenum == 0:
        while guess != number:
            guess = int(input("Guess my number from 1 to 20"))
            if guess > number:
                print("Too big")
            elif guess < number:
                print("Too small")
            elif guess == number:
                print("Great job u did it")
    elif primenum == 1:
        count = 0
        while guess != number:
            guess = int(input("Guess my number from 1 to 20"))
            if guess > number:
                print("Too big")
                count = count + 1
            elif guess < number:
                print("Too small")
                count = count + 1
            elif guess == number:
                if count <= 5:
                    print("Ur a genius")
                elif count <= 10:
                    print(" Well done good work")
                elif count <= 15:
                    print("Well done, finally you got it")



def main():
    global guess
    global number
    print("Im guessing a number")
    ran()
    while guess != number:
        ran()


main()
