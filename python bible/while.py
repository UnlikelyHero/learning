L = []

while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("The list is now Full")
print(L)
