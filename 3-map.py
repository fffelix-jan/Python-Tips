strings = ["broken", "pieces"]
print("Some strings:")
print(strings)
print("Now I will SMASH those strings to BITS! (a.k.a. just turn each one into a list of characters lol)")
strings = list(map(list, strings)) # run the list() function on each element in the strings list
print("look what we've got now:")
print(strings)