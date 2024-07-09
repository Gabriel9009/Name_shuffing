import random
print("Guess the correct word\n")
string = ["eniola", "tokoni", "standfast", "desmond", "ogolo", "ifeanyi"]


for i in string:
    mylist = list(i)
    random.shuffle(mylist)

    new = "".join(mylist)
    print(new, "\n")

    answer = input()

    if answer == i:
        print("corect")
    else:
        print("wrong")



