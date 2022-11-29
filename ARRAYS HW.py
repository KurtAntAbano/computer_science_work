    #def main():
    #    import random
    #    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     #   word = []
     #   for i in range(0,10):
    #        word.append(random.choice(alphabet))
    #    print(word)

    #    player_word = input("Input word with these numbers")
     #   score = 0
    #    for i in range(0, len(player_word)):
     #       if player_word[i] in word:
    #            score +=1
   #     print("You scored", score,"/10")

   # main()







#----------------------------------- doing car registration
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y',]


def run():
    registration = input("enter registration plate")
    if not length_check(registration) and not age_val(registration) and not area_code(registration, alphabet) \
            and not space_check(registration):
        run()
    else:
        print("valid")


def length_check(registration):
    if len(registration) == 8:
        return True
    else:
        return False


def area_code(registration, alphabet):
    count = 0
    if registration[0] in alphabet:
        count += 1
    if registration[1] in alphabet:
        count += 1
    if count == 2:
        print("TRUE")
        return True
    else:
        print("FALSE")
        return False


def age_check(registration):
    if 0 <= int(registration[2:4] <= 99):
        print("TRUE")
        return True
    else:
        print("FALSE")
        return False


def age_val(registration):
    age = registration[2:4]
    ans = age.isdigit()
    if ans:
        print("TRUE")
        return True
    else:
        print("False")
        return False

def space_check(registration):
    space = registration[4:5]
    if space == " ":
        print("True")
        return True
    else:
        print("False")
        return False

def rndm_letters():
    space = registration[5:9]
    if space.isalpha():
        return True
    else:
        return False

run()