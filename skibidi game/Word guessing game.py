import random

attempts = 0  # here u can use this if u decide to implement the point thing


def generateWordList():
    words = []  # define a list for our words

    file = open("dictionary.txt", "r")

    for line in file:  # goes over each line
        data = line.strip()  # splits it while stripping it (gets rid of white space)
        if len(data) <= 6:  # checks if the word is 6 letters or below
            words.append(data)  # add it to our awesome list
    # print(words) #uncommentthis if u want to see the whole list of words

    file.close()
    return words


def generateRanWord():
    wordList = generateWordList()  # now we have our list of words
    guessWord = random.choice(wordList)  # select a random word from the list
    print("This is the gueess word:" + guessWord)
    return guessWord


def main():
    guessWord = generateRanWord()  # get our guess word
    scrambledWord = scramble(guessWord)  # call our scramble function to jumble the words letters
    print("scrambled word:" + scrambledWord)  # prints scrambled word to the user
    guess = input("guess the unscrambled word")  # prompts user to guess
    verdict = validation(guess, guessWord)  # does a validation test to check if the user actually used all the letters given
    if verdict:  # if verdict returns true(user used the correct letters, then we can check if its actually in the right order)
        is_the_same(guess, guessWord)


def validation(guess, guessWord):
    used_letters = 0
    used_indices = []  # List to track used indices in guessWord

    if len(guess) != len(guessWord):
        print("Incorrect number of letters!")
        return

    for i in range(len(guess)):
        letter = guess[i] 

        # Check for matching letters in guessWord that haven't been used yet
        for z in range(len(guessWord)):
            if letter == guessWord[z] and z not in used_indices:
                used_letters += 1
                used_indices.append(z)  # Mark this index as used in guessWord
                break  # Move to the next letter in guess once a match is found

    # Check if the number of used letters equals the length of guessWord
    if used_letters == len(guessWord):
        print("You used the correct letters, yay!")
        return True
    else:
        print("What the sigma? You used incorrect letters or missed some!")
        return False


def is_the_same(guess, guessWord):
    if guess == guessWord:
        print("you guessed correctly YIPEE")
    else:
        print("guessed incorrectly GRRRR")


def scramble(guessWord):  # icl this was chatgpt
    word_list = list(guessWord)
    random.shuffle(word_list)
    scrambled_word = ''.join(word_list)

    return scrambled_word


main()

# HUGE NOTE
# its not finished lol but i basically did everything
# heres a list of what i missed /cba to do:
# user should have three attempts (failling the validation check, ie using all correct letters does not count
# as a failed attempt) only failed guesses count. litch just use a count variable or summit
# two failed attempts mean u get a new shuffled word
# the point system where player gains points depedning on whether they guess right
