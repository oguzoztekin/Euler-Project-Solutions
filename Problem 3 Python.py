#Problem 3

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    if n > 1:
        return n

number = 600851475143
largest_prime = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", largest_prime)