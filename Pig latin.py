ay = "ay"
way = "way"
constants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vowels = ["a","e","i","o","u"]

word = input("What word would you like to translate into piglatin?")
length = len(word)
word = word.lower()

if word[1] in vowels:
    print("theres a value")
