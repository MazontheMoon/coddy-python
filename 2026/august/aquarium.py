def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def calculate_penalty(violations):
    base = 50
    subtotal = base + 25 * violations
    if violations > 1:
        additional = subtotal * 0.10 * (violations - 1)
        total = subtotal + additional
    else:
        total = subtotal
    return int(total)

def factorial_mod(n, p):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p
    return result

def mod_inverse(a, p):
    # Using Fermat's little theorem: a^(p-1) ≡ 1 (mod p)
    # So a^(-1) ≡ a^(p-2) (mod p)
    return pow(a, p - 2, p)

def permutation_mod(n, r, p):
    if r > n:
        return 0
    
    # Calculate n! mod p
    numerator = factorial_mod(n, p)
    
    # Calculate (n-r)! mod p
    denominator = factorial_mod(n - r, p)
    
    # Calculate modular inverse of denominator
    inv = mod_inverse(denominator, p)
    
    # Result is (n! * inv((n-r)!)) mod p
    result = (numerator * inv) % p
    return result

def find_twin_primes(n):
    twin_pairs = []
    for i in range(2, n - 1):
        if is_prime(i) and is_prime(i + 2):
            twin_pairs.append((i, i + 2))
    return twin_pairs

# Read the calculation type
calc_type = int(input())

if calc_type == 1:
    violations = int(input())
    penalty = calculate_penalty(violations)
    print(penalty)

elif calc_type == 2:
    line = input().split()
    n = int(line[0])
    r = int(line[1])
    p = int(line[2])
    result = permutation_mod(n, r, p)
    print(result)

elif calc_type == 3:
    N = int(input())
    twin_pairs = find_twin_primes(N)
    for p1, p2 in twin_pairs:
        print(f"{p1} {p2}")