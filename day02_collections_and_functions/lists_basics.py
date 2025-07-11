numbers = [10, 20, 30]


print(numbers[0])
numbers.append(40)
print(numbers)


for n in numbers:
    print(n)


def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n

    return total


total = sum_list(numbers)
print(total)
