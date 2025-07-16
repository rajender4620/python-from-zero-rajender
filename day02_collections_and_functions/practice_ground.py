
#  Diclaring a variable in Python

name = 'superman'
released = 2025
ratings = 9.5
released = True


# since Python is dynamic it is smart enouught to know which type is when it is initialized
# it is inferenced
# with type() object we can know which type is in runtime
# Ex
# print(type(name))

# next
# with def one of the predefined keywork in python we can declare funtion


def say_hello(name):
    print('hello,{}'.format(name))
    return


say_hello('java')


def print_hero_name(name):
    print(f'hero Name is : {name}')
    return


print_hero_name('BatMan')

# loops


def print_with_loops(numbers):

    for num in numbers:
        print(f'NumBer is  {num}')

    return


def loops_with_range(numbers):
    for num in range(numbers):
        print(f'number are {numbers[2]}')
    return


def reverse_string(reversestrng):
    forreverseStrig = []

    # for str in reversestrng:
    #     print(str)
    # for str in range(len(reversestrng) - 1, -1, -1):
    #     print(str)
    # return    hrere i did mistake then i learned

    # for i in range(len(reversestrng) - 1, -1, -1):
    #     #  here when i use range then i will use i so that my mind get it to use index
    #     print(reversestrng[i])

    for i in range(10, 15, +1):

        #  hooo got it now how i can use this range()
        print(i)

    return


# print_with_loops([1, 3, 5, 5, 9, 65,])

def sum(a, b):
    total = 0
    total = a + b
    return total


# result = sum(9, 9)
# print(result)


# reverse_string('abcde')


# def print_even_numbers(n):
#     evenNums = []
#     #    logic for this is i module 2 we will always get evens
#     for i in range(0, n+1):
#         #  i think i need know how to chekc the bools in python
#         if i % 2 == 0:
#             evenNums.append(i)
#     return evenNums


# result = print_even_numbers(10)
# print(result)


# ✅ 2. Count vowels
# def count_vowels(word):
#     """
#     Count and return the number of vowels (a, e, i, o, u) in the given string
#     """
#     count = 0
#     # your code here
#     # for i in range(len(word) - 1,):
#     #     # here how to check multipleconditions
#     #     if (word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u'):
#     #         count += 1
#     #         print(word[i])

#     for i in range(len(word)):
#         if word[i] in 'aeiou':
#             count += 1
#     return count


# result = count_vowels('rajender')
# print(result)

# ✅ 3. Manual reverse, return
def manual_reverse(word):
    """
    Reverse a string manually using loop and return it
    """
    # revStr = ''
    revStr = []
    lastindex = 0
    # your code here
    # for i, w in enumerate(word):
    # print(f'sfd {i}, {w}')
    # print(f'lastIndex: {len(word) - 1}')
    # lastindex = len(word) - 1
    # revStr.append(word[lastindex])
    # lastindex = lastindex - 1
    # print(revStr)
    # revStr.append(word[])
    # for char in word:
    #     revStr = char + revStr
    for char in word:
        revStr.insert(0, char)
        print(revStr)

    return ''.join(revStr)


# result = manual_reverse('someword')
# print(result)

def manual_sum(numbers):
    totalSumVal = 0
    """
    Compute sum of numbers manually (with loop)
    """
    # your code here

    for num in numbers:
        totalSumVal = num + totalSumVal
    return totalSumVal


# result = manual_sum([1, 4, 6, 9])
# print(result)

def print_movie_info():
    """
    Create a dictionary and print all key: value pairs
    """
    movie = {
        'title': 'Inception',
        'year': 2010,
        'rating': 8.8
    }
    # print keys and values here

    print(movie.get(movie['title']))
    print(movie.get(movie['rating']))
    print(movie.get(movie['year']))
    print(movie['year'])
    print(movie.keys())

    # for movi in movie:
    #     print(f'movie kesy: {movie.keys()} , movie vals : {movie.values()}')
    for key, val in movie.items():
        print(f'movie key : {key} , movie val : {val}')
    return


# print_movie_info()

# ✅ 7. Unique letters
def unique_letters(word):
    uniqueLettes = ''
    """
    Return a set of unique letters in the word
    """
    # your code here
    for wor in word:
        if wor not in uniqueLettes:
            uniqueLettes = uniqueLettes + wor
    return uniqueLettes


result = unique_letters('rajender')
print(result)
