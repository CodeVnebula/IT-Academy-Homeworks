import datetime

# For first empty line in console
print()
year = int(input("Enter year of birth: "))

isLeap = False      # by default let's say year isn't leap

if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    isLeap = True       # If year is leap 'isLeap' becomes true

while True:
    month = int(input("Enter month of birht 1/12: "))       # To make sure user doesn't enter wrong data for month
    if month >= 1 and month <= 12:
        break

if (month == 1) or (month == 3) or \
   (month == 5) or (month == 7) or \
   (month == 8) or (month == 10) or (month == 12):      # Months: Jan, Mar, May, Jul, Aug, Oct, Dec - 31 days
        while True:
             day = int(input("Enter day of birth: "))
             if day >= 1 and day <= 31:         # Min valid input = 1, Max valid input = 31
                break
elif month == 2:        # Case February
     if isLeap:
          while True:
             day = int(input("Enter day of birth: "))   # If leap Min valid input = 1, Max valid input = 29
             if day >= 1 and day <= 29:                 
                break
     else:
          while True:
             day = int(input("Enter day of birth: "))   # If not leap Min valid input = 1, Max valid input = 31
             if day >= 1 and day <= 28:
                break
             
else:
    while True:                                         # Rest of the months - days = 30
             day = int(input("Enter day of birth: "))
             if day >= 1 and day <= 30:         # Min valid input = 1, Max valid input = 30
                break
             
              # To print date perfectly
if day < 10 and month < 10:
    print("Date: 0", day, ".0", month, ".", year, sep="")   # Case - D.M.YYYY
elif day < 10 and month >= 10:
    print("Date: 0", day, ".", month, ".", year, sep="")   # Case - D.MM.YYYY
elif day >= 10 and month >= 10:
    print("Date: ", day, ".", month, ".", year, sep="")   # Case - DD.MM.YYYY
else:
    print("Date: ", day, ".0", month, ".", year, sep="")   # Case - DD.M.YYYY

date = datetime.datetime(year, month, day)
week_day = date.strftime("%A")    # Getting a week day
print("Day of week: ", format(week_day), sep="", end="\n\n")    # Printing week day
