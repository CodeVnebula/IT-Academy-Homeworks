import random
while True:
    gamers_quantity = int(input("Enter, how many players? "))
    if gamers_quantity > 0:
        break

for i in range(1, gamers_quantity + 1):
    print(f"Player # {i} - Pair of dice: ", end="")
    for j  in range(2):
        print(random.randint(1, 6), ' ', end="")
    print()   