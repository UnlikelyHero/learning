user_list = []


def add_user(name):
    if name in user_list:
        print("You've already listed {}.".format(name))
    else:
        user_list.append(name)


while True:
    name = input("Enter a name to add to the list, otherwise enter 0 to stop.").strip().capitalize()

    if name != "0":
        add_user(name)
        print(user_list)
    else:
        break
