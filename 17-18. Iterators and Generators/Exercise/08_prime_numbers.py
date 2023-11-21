def get_primes(numbers: list[int]):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in numbers:
        if is_prime(num):
            yield num


# Test case 1
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Test case 2
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
