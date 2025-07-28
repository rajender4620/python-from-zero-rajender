# try:
#     num = int(input("Enter a number: "))
#     print("Your number:", num)
# except ValueError:
#     print("That's not a number.")


# try:
#     x = int(input("Enter dividend: "))
#     y = int(input("Enter divisor: "))
#     result = x / y
# except ZeroDivisionError:
#     print("Division by zero not allowed.")
# else:
#     print("Result:", result)
# finally:
#     print("Thanks for using the calculator.")


# try:
#     my_list = [1, 2, 3]
#     print(my_list[5])
# except IndexError as e:
#     print("Index error:", e)

# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print("Valid age:", age)


# try:
#     check_age(-3)
# except ValueError as e:
#     print("Error:", e)


# def divide(a, b):
#     assert (b != 0), "Cannot divide by zero"
#     return a / b


# print(divide(10, 0))
