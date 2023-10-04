number = int(input("1) Square\n2)Triangle\nEnter a number:"))
if number == 1 :
    lengthsquare = int(input("Input a length"))
    areasquare = lengthsquare * lengthsquare
    print("The area of the square is", areasquare)

elif number == 2:
    basetriangle = int(input("Input base"))
    heighttriangle = int(input("Input height"))
    areatriangle = (basetriangle * heighttriangle) / 2
    print("The area of the triangle is", areatriangle)

else:
    print(" invalid number")

