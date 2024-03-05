while True:
    n_term = int(input("Enter n between [0, 20]: "))
    if 0 <= n_term <= 20:
        break

first = 0 
second = 1

for i in range(2, n_term + 1):
    next_ = first + second
    first = second
    second = next_

print(next_) 
