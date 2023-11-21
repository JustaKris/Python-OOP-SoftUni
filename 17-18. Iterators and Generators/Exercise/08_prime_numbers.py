def get_primes(numbers: list):
    for num in numbers:
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


# Test case 1
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Test case 2
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
