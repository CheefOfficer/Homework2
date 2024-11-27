numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for e in numbers:
    is_prime = True
    if e == 1:
        continue
    else:
        for j in range(2, e-1):
            if e % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(e)
    else:
        not_primes.append(e)

print("Numbers: ", numbers)
print("Primes: ", primes)
print("Not Primes: ", not_primes)







