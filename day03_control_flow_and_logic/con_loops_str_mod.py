
def check_age(age):
    if (age > 10):
        print('big')
    elif (age == 10):
        print('Exactly 10')
    elif age >= 10 and age <= 19:
        print('Between 10 and 19')
    elif 75 <= age <= 80:
        print('Old')
    return


"""
Print length → len(text)

Print first char → text[0]

Print last char → text[-1]

Print first 6 letters → text[0:6]

Print from index 7 to end → text[7:]
"""
text = "python learner"

print(len(text))
print(text[0])
print(text[-1])
print(text[0:6])
print(text[7:])
print(text.upper())
print(text[0].upper())
print(text.replace('learner', 'developer'))
print(text.find('o'))
print(text.split(" "))


def count_a(s):
    count = 0
    for val in s:
        if val == 'a':
            count += 1
    print(count)
    return count


# count_a('a')
# print(text.count('a'))


def is_palindrome(pal_text):
    print(len(pal_text))
    length = len(pal_text)
    print(len(pal_text)-1)
    print(length - 1)
    print(length // 2)
    for i in range(length // 2):
        print(f"Comparing {pal_text[i]} with {pal_text[length - 1 - i]}")
        if pal_text[i] != pal_text[length - 1]:
            return False
    return True


def is_pal_using_slice(pal_text):

    return pal_text == pal_text[::-1]


def isPal(string):
    if (string == string[::-1]):
        return True
    return False


# print(isPal("goog"))





