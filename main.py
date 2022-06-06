# menu:
# small pizza - 550
# medium pizza - 850
# large pizza - 1200
# pepperoni on small pizza - 200
# pepperoni on medium and large - 300
# extra cheese on any pizza size - 100

print("Welcome to the Python Pizza Deliveries")
size = input("Which pizza size do you want prepared? S, M or L : ").upper()
pep = input("Would you want pepperoni on your pizza? Y or N : ").upper()
cheese = input("Would you want extra cheese on your pizza? Y or N : ").upper()
total = 0

if size == "S":
    total = 550
elif size == "M":
    total = 850
elif size == "L":
    total = 1200
else:
    print("Please enter a valid pizza size.")

if pep == "Y" and size == "S":
    total += 200
elif pep == "Y" and size == "M" or "L":
    total += 300

if cheese == "Y":
    total += 100

print(f"Your total bill is {total}/=")
