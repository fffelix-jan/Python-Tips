def describe_someone(name, *args):
    for elem in args:
        print(f"{name} is {elem}!")

def describe_several_people(**kwargs):
    for person, description in kwargs.items():
        print(f"{person} is {description}!")


# using *args, we can add as many positional arguments as we want
describe_someone("Tobias", "first here", "smart")

# using **kwargs, we can add as many keyword arguments we want
describe_several_people(Olivia="funny", Gelila="charming", Nathan="happy")

# we can also unpack a list or tuple to use as positional arguments
# the * unpacks a list or tuple to use as args
args_to_use = []
print("Enter 5 ways to describe Nathan, pressing Return after each one.")
for i in range(5):
    args_to_use.append(input())
describe_someone("Nathan", *args_to_use)    # unpack the list to use as args

