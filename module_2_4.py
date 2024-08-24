numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
a = 2
for i in range(len(numbers) + 1):
    if i >= 2:
        while a <= (i ** 0.5):
            if i % a == 0:
                is_prime = False
                break
            a += 1
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)
        is_prime = True
        a = 2
print(primes)
print(not_primes)
