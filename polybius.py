# TASK 1 AND 2
square = [[0, 1, 2, 3, 4, 5],
          [1, "A", "B", "C", "D", "E"],
          [2, "F", "G", "H", "I", "J"],
          [3, "K", "L", "M", "N", "O"],
          [4, "P", "Q", "R", "S", "T"],
          [5, "U", "V", "W", "X", "Y"],
          [6, "Z", "?", " ", "@", "."]]


def display(square):
    for i in range(0, len(square)):
        print(square[i])


def deCipher(cryptogram, square):
    cryptogram = cryptogram.replace(" ", "")  # remove spaces
    crypto = cryptogram.split(",")  # split by comma and change converts to a list

    word = ""  # initialise the value of word to empty string

    # .......................... MISSING CODE   ..................................
    #
    #
    #
    #
    #
    #                         Write the missing code
    for i in range(0, len(crypto)):
        str_crypto = str(crypto[i])
        word += square[int(str_crypto[0])][int(str_crypto[1])]

    return word


def main():
    display(square)

    code = input(" Enter Cryptogram (the ciphered message) ...  ")

    print("The Secret word is ... " + deCipher(code, square))


main()
