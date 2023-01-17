def createUsername():
    first_name = input("Input first name")
    last_name = input("input last name")
    num = 0
    username = last_name + first_name[0] + str(num)
    unique = existingUser(username)
    while unique == False:
        num += 1
        username = last_name + first_name[0] + str(num)
        unique = existingUser(username)
    print("Username is unique")







