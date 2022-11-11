airport_codes = {'LHR':'London Heathrow', 'MAN':'Manchester','BHX':'Birmingham','EDI':'Edinburgh','LTN':'London'}

def add_new():
    new_code = input("What is the new code?")
    new_key = input("Where is the airport")

    length = len(new_code)
    if length != 3:
        print("error")
        add_new()
    elif length == 3:
        airport_codes[new_code] = new_key

    print("the new codes are:",airport_codes)


def search():
    code = input("What is the code?")
    output = airport_codes.get(code)
    print(output)



def exit():
    print("thank you for using my program!")


def menu():
    answer = input("Choose an option: \n1. Add a new airport?\n2. Search for an airport?\n3. exit\n")

    if answer == '1':
        add_new()
    elif answer == '2':
        search()
    elif answer == '3':
        exit()
    else:
        menu()



menu()