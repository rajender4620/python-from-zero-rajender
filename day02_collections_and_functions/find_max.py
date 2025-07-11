def find_max(numbers):
    max_num = numbers[0]

    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num


result = find_max([10, 20, 5, 7])
print(result)
