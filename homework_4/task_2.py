import random

while True:
    number = int(input("Enter n between 0-30: "))
    if number > 0 and number < 30:
        break

generated_numbers = []

for _ in range(number):
    generated_numbers.append(random.randint(0, 1000))

print(generated_numbers)
print(max(generated_numbers))
