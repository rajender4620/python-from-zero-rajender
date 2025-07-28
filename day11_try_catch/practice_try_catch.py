data = {"name": "Rajender", "age": 28}


# try:
#     user_input = input("Enter the key ")
#     if user_input not in data:
#         raise ValueError("Please enter string")
#     else:
#         print(data[user_input])
# except ValueError as e:
#     print("invalid key: ", e)


# try:
#     key = input("Enter the key ")
#     print("Value:", data[key])
# except KeyError:
#     print("❌ Key not found in data.")


# def division(a, b):
#     try:
#         a = int(input("enter a :"))
#         b = int(input("enter b :"))

#     except ValueError as e:
#         print("error :", e)


# def division(a, b):
#     while True:
#         try:
#             a = int(input("Enter a: "))
#             b = int(input("Enter b: "))
#             result = a / b
#         except ValueError:
#             print("❌ Invalid input. Please enter integers only.")

#         except ZeroDivisionError:
#             print("❌ Cannot divide by zero.")
#         else:
#             print("✅ Result:", result)
#             print("✔️ Operation complete.")
#             break


