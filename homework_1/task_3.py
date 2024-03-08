import math

print("Enter the sides of triangle:")

while True:
    side_1 = int(input("Enter side 1: "))
    if side_1 > 0:
        break
while True:
    side_2 = int(input("Enter side 2: "))
    if side_2 > 0:
        break
while True:
    side_3 = int(input("Enter side 3: "))
    if side_3 > 0:
        break

if ((side_1 + side_2 <= side_3) or (side_1 + side_3 <= side_2) or (side_3 + side_2 <= side_1)):
    print("This kind of triangle doesn't exist!")
else:
    perimeter = side_1 + side_2 + side_3
    
    semi_perimeter = perimeter / 2                    
    area = math.sqrt(semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3))
    print("Perimeter of triangle:", perimeter, "\nArea of triangle:", area)