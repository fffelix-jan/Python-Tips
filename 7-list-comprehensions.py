people = ["Olive", "Otto", "Olympia", "Otis", "Todd", "Weird Tom", "Shapeshifter"]
odd_squad_agents = [e for e in people if e[0].upper() == "O"]   # filter out only the names that start with "O"
the_exact_same_agents = [e for e in odd_squad_agents]     # or just copy everything without checking anything
print(odd_squad_agents)
print(the_exact_same_agents)

nums = [1, 2, 3, 4]
tripled_nums = [e * 3 for e in nums]  # make a new list, tripling everything in the old list
print(tripled_nums)

sounds = ["baa ", "moo ", "oink "]
repeated_sounds = [e * 2 for e in sounds]
print(repeated_sounds) 