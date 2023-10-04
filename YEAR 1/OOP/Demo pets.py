# Demo on OOP
class Pets():  # the class always starts with a capital letter
    def __init__(self, givenName, givenAge):  # __init__ is a constructor , self is the object
        self.name = givenName  # name can be easily changed by: object.name = "new name" as it is public unlike __age
        self.__age = givenAge  # age is private, if we want to change we use set_age

    def describe(self):  # self is like the object
        return self.name + " I am " + str(self.__age) + " years old"

    # print(myPet.describe()) would print this string

    def speak(self, sound):
        print(self.name + " says " + sound)
        # a commonn mistake is putting self.sound, this is incorrect as sound is a variable, not an attribute

    def sleep(self):  # all Pets sleep silently
        print("Sleeping Silently")

    def ask(self, question):
        return (question)

    # be mindful of return, don't forget to print

    def set_age(self, newAge):  # set and get allow us to access private attributes/ methods
        self.__age = newAge  # set can change the value

    def get_age(self):  # get can display the value
        return self.__age


# myPet = Pets("Max", 5) will create a pet named max with the age 5
# myPet = (is an example of Instantaion

class Dog(Pets):  # dog inherits  all attributes and methods from Pets

    def __init__(self, givenspecies, givenname, givenage):
        self.species = givenspecies
        number_of_legs = 4  # all dogs have 4 legs (constant)
        super().__init__(givenname, givenage)  # create a pet, then make it a dog
        #  super().__init__ means go to super() which is Pets then make a pet

    def bark(self):
        print(" Woof .... Woof...Woof")


class Cat(Pets):  # Cat also inherits  attributes and methods from pets, in the brackets of the Cat is the super

    def __init__(self, givenbread, givenname, givenage):
        self.bread = givenbread
        number_of_legs = 4  # all cats have 4 legs
        super().__init__(givenname, givenage)

    def meow(self):
        print(" Meow .... meow..... Meow")

    def sleep(self):
        print("my name is  " + self.name +
              " I am closing my eyes slowly and ... Snore....Snore....Snore")
        # sleep() is already in the super class, but in this instance we want it to snore,
        # this new sleep() overwrites the sleep() that was inherited from the super class
        # this is polymorphism


if __name__ == '__main__':
    myDog = Dog("Bull dog", "Max", 8)
    myCat = Cat("Birman Cat", "Felix", 3)

    # print("the dog: " +myDog.species + " ... \n" + myDog.describe(),
    # "\nthe cat: " +myCat.bread + " says ...\n  " + myCat.describe())
    myDog.speak("hello everyone I can Bark .. ")
    # myDog.bark()
    # myDog.sleep()
    # myCat.meow()
    # myCat.sleep()
    # myDog.ask(myCat.meow())    # interaction
    # myCat.ask(myDog.bark())    # interaction

    ############################################
    # trying methods which are not exist
    # print(myDog.colour)
    # myDog.breathe()
    ############################################

    ############################################
# using setter and getter
# print("my age before is " + str(myDog.get_age()))
# myDog.set_age(6)
# print("now my age is " +str(myDog.get_age()))

#############################################
