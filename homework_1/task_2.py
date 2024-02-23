import datetime

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

# current_year = int(input("Enter current year: "))
# age = current_year - birth_year

current_year = datetime.datetime.now().year
age = current_year - birth_year

print("Hello", name, "You are", age, "years old")

