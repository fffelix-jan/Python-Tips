import sys

my_list = ["apple", "banana", "carrot"]

try:
    to_print = int(input("Please enter 0 for apple, 1 for banana, or 2 for carrot."))
    print(my_list[to_print])
except IndexError as e: # "as e" is optional, you can save the exception to a variable
    print("You tried to choose something that wasn't in the list! Python gave this nasty error:")
    print(e)    # the exception could be printed for debugging purposes
except: # to catch ANY exception
    print("Something else went wrong! You probably typed in something that wasn't an integer!")

print("But I'm gonna carry on running anyways...")

for index, elem in enumerate(my_list):  # you can loop through the index and the element at the same time with enumerate()
    print(f"At index {index} you will find {elem}...")

try:
    print("OK, let me try quitting now...")
    sys.exit(0)
except:
    print("Jokes on you, you can't use sys.exit(0) when you are catching any exception! You need to catch the specific exception.")

print("OK, I can actually quit now")
sys.exit(0)
print("this line will not be printed")