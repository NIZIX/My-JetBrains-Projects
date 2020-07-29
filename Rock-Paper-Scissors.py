import random

def Game(option):

    global list_of_things, points

    list_len = len(list_of_things)
    list_len = list_len / 2
    rand_choise = random.choice(list_of_things)

    left_field = list_of_things[list_of_things.index(option) - 1 if list_of_things.index(option) != 0 else list_of_things.index(option) : 0 if int(list_of_things.index(option)) - int(list_len) <= 0 else int(list_of_things.index(option)) - int(list_len) - 1 : -1]
    right_field = list_of_things[list_of_things.index(option) + 1 : int(list_of_things.index(option)) + int(list_len) + 1 : 1]
    
    if len(right_field) >= len(left_field):
        if rand_choise in right_field:
            return "Sorry, but computer chose {}".format(rand_choise)
        elif rand_choise == option:
            points += 50
            return "There is a draw ({})".format(rand_choise)
        else:
            points += 100
            return "Well done. Computer chose {} and failed".format(rand_choise)
    else:
        if rand_choise in left_field:
            points += 100
            return "Well done. Computer chose {} and failed".format(rand_choise)
        elif rand_choise == option:
            points += 50
            return "There is a draw ({})".format(rand_choise)
        else:
            return "Sorry, but computer chose {}".format(rand_choise)


name = input("Enter your name: ")
print("Hello, " + name)
file = open("rating.txt")

for line in file:
    if name in line:
        points = int(line.split()[1])
        break
    else:
        points = 0

file.close()

list_of_things = input().split(",")
if list_of_things == [""]:
    list_of_things = ["scissors", "rock", "paper" ]

print("Okay, let's start")

while True:
    player_choise = input()
    if player_choise == "!exit":
        break
    if player_choise == "!rating":
        print("Your rating: " + str(points))
        continue
    if not (player_choise in list_of_things):
        print("Invalid input")
        continue
    print(Game(player_choise))

print("Bye!")
