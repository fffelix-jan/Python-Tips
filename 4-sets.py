my_set = set() # this makes an empty set
my_set = {"apple", "banana"} # a way to initialize a set
my_set = set(["apple", "banana"]) # another way to initialize a set, using the elements in a list
my_set.add("orange") # add something to the set
my_set.remove("banana") # remove something from the set

to_check = input("Enter something to check if it's in the set: ")

# you could also do "if x in y" with a list
# although using a set is faster
if to_check in my_set:  
    print("Yes, it is in the set!")
else:
    print("No, it isn't in the set!")