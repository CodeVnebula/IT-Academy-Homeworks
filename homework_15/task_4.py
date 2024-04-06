def count_vovels(string):
    count = 0
    print(string, "-> ", end="")
    vovels = ['a', 'e', 'i', 'o', 'u']
    for char in string.lower():
        if char in vovels:
            count += 1
    return count

def main():
    print(count_vovels("Test"))
    print(count_vovels("Python"))
    print(count_vovels("Kvaratskhelia"))

if __name__ == "__main__":
    main()
