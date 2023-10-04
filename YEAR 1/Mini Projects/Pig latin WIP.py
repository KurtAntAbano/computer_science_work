ay = "ay"
way = "way"
constants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vowels = ["a","e","i","o","u"]

word = input("Write a sentence to convert into pig latin").lower()
individual_words = word.split()
length = len(individual_words)
print(length)
print(individual_words)
list =[]
for i in range(0,length):
    if individual_words[0] in constants:
        remove_first_letter = individual_words[1:length]
        pig_latin = remove_first_letter + word[0] + "ay"
        list.append(str(pig_latin))

    elif individual_words[0] in vowels:
        pig_latin = individual_words + "ay"
        list.append(str(pig_latin))

print(list)
