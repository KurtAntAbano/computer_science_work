def linear_search(data_set, name):
    index = -1
    i = 0
    found = False
    while i < len(data_set) and found == False:
        if data_set[i] == name:
            index = i
            found = True
        i += 1
    return index


isFound = (linear_search(["Bob", "Kyle", "Liam", "Patrick", "Ben", "Kurt", "Andrew"], "Kurt"))
if isFound != -1:
    print(f"name has been found at index {isFound}")
else:
    print("name could not be found")
