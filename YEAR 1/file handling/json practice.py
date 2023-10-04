import json

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict = json.loads(person)  # converts json to python dictionary

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])



with open('myfile.txt', 'r') as f:
  data = json.load(f)  # load( ) is used to read, loads( ) used to convert

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)
