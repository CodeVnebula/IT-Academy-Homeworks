import datetime
import sys                 # for sys.exit() function
from forex_python.bitcoin import BtcConverter

# For first empty line in console
print()
year = int(input("Enter year, when you bought Bitcoin: "))

isLeap = False      # by default let's say year isn't leap

if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    isLeap = True       # If year is leap 'isLeap' becomes true

while True:
    month = int(input("Enter month, when you bought Bitcoin 1/12: "))       # To make sure user doesn't enter wrong data for month
    if month >= 1 and month <= 12:
        break

if (month == 1) or (month == 3) or \
   (month == 5) or (month == 7) or \
   (month == 8) or (month == 10) or (month == 12):      # Months: Jan, Mar, May, Jul, Aug, Oct, Dec - 31 days
        while True:
             day = int(input("Enter day, when you bought Bitcoin: "))
             if day >= 1 and day <= 31:         # Min valid input = 1, Max valid input = 31
                break
elif month == 2:        # Case February
     if isLeap:
          while True:
             day = int(input("Enter day, when you bought Bitcoin: "))   # If leap Min valid input = 1, Max valid input = 29
             if day >= 1 and day <= 29:                 
                break
     else:
          while True:
             day = int(input("Enter day, when you bought Bitcoin: "))   # If not leap Min valid input = 1, Max valid input = 31
             if day >= 1 and day <= 28:
                break
             
else:
    while True:                                         # Rest of the months - days = 30
             day = int(input("Enter day, when you bought Bitcoin: "))
             if day >= 1 and day <= 30:         # Min valid input = 1, Max valid input = 30
                break

if year <= 2012 or (year == 2013 and month < 10):        # Forex library btc price history before 2013.10.01 isn't avilable
        print("Unfortunately we don't have data of Bitcoin price before 01.10.2013! Please Enter date after given date))", end="\n\n")
        sys.exit(0)

current_date = datetime.date.today()

if (year > current_date.year) or \
   (year == current_date.year and month > current_date.month) or \
   (year == current_date.year and month == current_date.month and day > current_date.day):
    print("The date you've entered hasn't come yet! Please enter date correctly!!!", end="\n\n")
    sys.exit(0)

while True:
    usd_paid = int(input("Enter Amount of USD you paid for bitcoin: "))
    if usd_paid > 0:
        break



print()            
              # To print date perfectly
if day < 10 and month < 10:
    print("Date of buying Bitcoin: 0", day, ".0", month, ".", year, sep="")   # Case - D.M.YYYY
elif day < 10 and month >= 10:
    print("Date of buying Bitcoin: 0", day, ".", month, ".", year, sep="")   # Case - D.MM.YYYY
elif day >= 10 and month >= 10:
    print("Date of buying Bitcoin: ", day, ".", month, ".", year, sep="")   # Case - DD.MM.YYYY
else:
    print("Date of buying Bitcoin: ", day, ".0", month, ".", year, sep="")   # Case - DD.M.YYYY




date_purchased = datetime.datetime(year, month, day)

print("Current date: ", current_date, end="\n\n")





bitcoin = BtcConverter()
btc_previous_price = bitcoin.get_previous_price("USD", date_purchased)  # gets 1btc price in usd (previous)
latest_price = bitcoin.get_latest_price("USD")                          # gets 1btc price in usd (latest)

print("Price of 1BTC before: ", btc_previous_price, "$")
print("Price of 1BTC currently: ", latest_price, "$", end="\n\n")


"""
    quantity of bought btc (previous) will be   
                            
                       calculating:     quantity_of_bought_btc = usd_paid / btc_previous_price
                                        
                                        amount_of_usd_now = quantity_of_bought_btc * latest_price

                                        profit = amount_of_usd_now - usd_paid

                    
                    
                    example: usd_paid = 10$,  btc_previous_price = 2$, latest_price = 5$...

                             quantity_of_bought_btc = 10 / 2,,,,,, quantity_of_bought_btc = 5...... we got 5 btc yay

                             amount_of_usd_now = 5 * 5......    amount_of_usd_now = 25$

                             profit = 25 - 10.....  profit = 15$

                             if amount_of_usd_now < paid_usd  for example:  if latest_price = 1$,  quantity_of_bought_btc = 1.

                                    amount_of_usd_now = 5 * 1......    amount_of_usd_now = 5$
                                    
                                    profit = 5 - 10.... profit = -5$.... so we have some money loss here (((:

"""


quantity_of_bought_btc = usd_paid / btc_previous_price

amount_of_usd_now = quantity_of_bought_btc * latest_price

profit = amount_of_usd_now - usd_paid

if profit > 0:
    print("You earnt +", profit, "$")
elif profit == 0:
    print("You earnt ", profit, "$")
else:
    print("You loss -", profit, "$")

print()
