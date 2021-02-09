flavour_dictionary = {
    "apple" : "sweet and somewhat tart",
    "orange" : "sour, juicy and tangy",
}

# add something to the dictionary
flavour_dictionary["durian"] = "eww"

try:
    check = input("What fruit would you like a description of?: ")
    print(flavour_dictionary[check])
except KeyError:
    print("That fruit is not in the dictionary.")

# You can even for loop through a dictionary's keys:
for fruit in flavour_dictionary:
    print("Here's a fruit:", fruit)

# Or, you can loop through the keys and their values:
for fruit, description in flavour_dictionary.items():
    print(fruit, "is described as", description)

# Convert the keys to a list:
fruits_list = list(flavour_dictionary.keys())
print(fruits_list)

# Or convert the values in the dictionary to a list:
fruity_descriptions_list = list(flavour_dictionary.values())
print(fruity_descriptions_list)

# Or get a list of tuples (which are like lists):
list_of_both = list(flavour_dictionary.items())
print(list_of_both)