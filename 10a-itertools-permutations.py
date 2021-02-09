import itertools

string = "radar"

# join the lists of characters, as the permutations are lists of characters
string_permutations = ["".join(elem) for elem in itertools.permutations(string)]   
unique_perms = set(string_permutations) # sets have no duplicates
unique_perms = list(unique_perms) # we can make it a list again if we want

print(unique_perms)