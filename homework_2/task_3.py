car_speed = int(input("Enter the velocity of the car: "))

if car_speed > 0:
    if car_speed > 120:
        print("Category: very fast")
    elif car_speed > 60:
        print("Category: fast")
    elif car_speed > 30:
        print("Category: moderate")
    else:
        print("Category: slow")
else:
    print("Let's put the car in the first gear :)")

