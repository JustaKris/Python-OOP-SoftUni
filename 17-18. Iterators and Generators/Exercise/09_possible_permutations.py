def possible_permutations(input_list: list):
    if len(input_list) <= 0:
        yield input_list
    else:
        for i in range(len(input_list)):
            for perm in possible_permutations(input_list[:i] + input_list[i + 1:]):
                yield [input_list[i]] + perm


# Test case 1
[print(n) for n in possible_permutations([1, 2, 3])]

# Test case 2
[print(n) for n in possible_permutations([1])]
