my_tuple = ("apples", "oranges")

# creating a new tuple in place of the old one is ok...
my_tuple = ("apples", "oranges", "durian")

print(my_tuple)

# but editing it is not
del my_tuple[2] # raises an exception