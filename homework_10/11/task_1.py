while True:
    n = int(input("Enter n (n > 1): "))
    if n > 1:
        break

x = 0
sign = 1    # For changing value of 1 to  -1 and vice versa

for i in range(1, n + 1):
    x += sign * (1 / (2 * i - 1))       # On each iteration we get sum of this function 
    sign *= -1  # Every second iteration sign changes                     (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )      
x *= 4
print(f"For n = {n}, x = {x}")
