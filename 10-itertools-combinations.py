import itertools

people = ["Bevis", "Nina", "Olivia", "Gelila", "Russell"]

possible_group_project_teams = list(itertools.combinations(people, 2))

print("Group project pairs:")

for elem in possible_group_project_teams:
    print(elem)