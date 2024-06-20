cached_sequence = {}

def generate_sequence_use_cache(n):
    original_n = n
    if n in cached_sequence:
        return cached_sequence[n]  
    
    sequence = [n]  
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
        sequence.append(n)
    
    cached_sequence[original_n] = sequence 
    
    return sequence


def generate_sequence(n):
    sequence = []
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n) + 1
        sequence.append(n)
    return sequence


def main():
    print(cached_sequence)
    n = int(input("Enter n: "))
    sequence = generate_sequence_use_cache(n)
    
    print("Sequence for", n, ":", sequence)

if __name__ == "__main__":
    main()
