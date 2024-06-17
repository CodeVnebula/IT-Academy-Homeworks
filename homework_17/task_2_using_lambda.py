"""
    With using lambda/map functions 
"""

from random import randrange

def main():
    
    list_one = list(map(lambda element: randrange(1, 10), range(randrange(10, 20))))
    list_two = list(map(lambda element: randrange(1, 10), range(randrange(10, 20))))
    list_three = list(map(lambda element: randrange(1, 10), range(randrange(10, 20))))
    print(list_one)
    print(list_two)
    print(list_three)
    sums = list(map(lambda a, b, c: (a + b + c), list_one, list_two, list_three))
    print(sums)
        
if __name__ == "__main__":
    main()
