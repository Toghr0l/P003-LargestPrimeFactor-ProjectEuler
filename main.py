# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def calculate_prime_factors(N):
    prime_factors = set()
    if N % 2 == 0:
        prime_factors.add(2)
        while N % 2 == 0:
            N = N // 2
    for i in range(3, int(N ** (0.5)) + 1, 2):
        while N % i == 0:
            prime_factors.add(i)
            N = N // i
    if N > 2:
        prime_factors.add(N)
    return prime_factors

print(f"Prime facotrs of 600851475143 are: {calculate_prime_factors(600851475143)}")
max = max(calculate_prime_factors(600851475143))
print(f"Max is {max}")