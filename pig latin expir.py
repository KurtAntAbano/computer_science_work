ay = "ay"
way = "way"
constants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vowels = ["a","e","i","o","u"]

word = input("What word would you like to translate into piglatin?").lower()
length = len(word)

if word[0] in constants:
    remove_first_letter = word[1:length]
    pig_latin = remove_first_letter+word[0]+"ay"

elif word[0] in vowels:
    pig_latin = word+"ay"

print(pig_latin)

