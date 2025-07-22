

# i = 1
# while i < 10:
#     i += 1
#     if i == 8:
#         break
#     if i == 3:
#         continue
#     print(i)


"""
✅ 1. Print all even numbers from 1 to 50
Output: 2, 4, 6, ..., 50

Use while only

No range() allowed

Print in a single line
"""

# while i < 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1

"""✅ 2. Count the number of digits in a given number
Example Input: 123456
Output: 6

Use integer division

No string conversion allowed
"""


# print(10 % 4)
# print(10 // 4)
# print(10 / 4)


# def count_number(inpt):
#     count = 0
#     while inpt > 0:
#         print(f'before {inpt}')
#         inpt = inpt // 10
#         print(f'after {inpt}')
#         count += 1

#     return count


# print(count_number(123456))


"""✅
3. Reverse a number
Input: 1234 → Output: 4321

Do it with while

No slicing or strings

"""


# def reverse_num(num):

#     rev = 0

#     while num > 0:
#         last_digit = num % 10
#         rev = rev * 10 + last_digit
#         num = num // 10
#     return rev


# print(reverse_num(1234))


def is_palindrome_number(num):

    orginal = num
    rev = 0
    while num > 0:
        lastdig = num % 10
        rev = rev * 10 + lastdig
        num = num // 10

    if orginal == rev:
        return True

    return False


print(is_palindrome_number(121))


def facto(num):
    fact = 0
    total = 1
    originamnum = num
    while num > 1:
        total = total * num
        num -= 1
    print(total)
    return


facto(5)
