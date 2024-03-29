import random
import math

while True:
    n = int(input("Enter n (n > 1): "))
    if n > 1:
        break

counter = 0

for i in range(0, n):
    a = random.random()
    b = random.random()
    distance = math.sqrt(a ** 2 + b ** 2)   # Distance from the origin point (0, 0) to (a, b) generated point
    if distance <=1:
        counter += 1

output = 4 * counter / n
print(f'Output: {output}')      
