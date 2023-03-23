
import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file) # dump( ) allows us to write in a JSON file
  #  here we are adding the dictionary to person.txt



with open('person.txt', 'r') as x:
  data = json.load(x)  # load( ) allows us to read a JSON file


print(data)