# file = open(
#     "C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "r")
# content = file.read()
# file.close()
# print(content)


# with open("C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "r") as f:
#     content = f.readlines()
#     count = 0
#     for con in content:
#         print(con.strip())
#         count += 1

#     print(f"Total line are : {count}")

# with open("C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "a") as f:
#     f.write("Discipline is choosing what you want most over what you want now.\n")
#     f.write("You don’t have to be extreme, just consistent.\n")


# with open('C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt', 'r') as f:
#     content = f.read()
#     list = []
#     for i in range(0, 10):
#         list.append(content[i])

#     result = "".join(list)
#     print(result)


# with open('C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt', 'r') as f:
#     content = f.read()
#     freq_word = {}
#     words = content.split()

#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         freq_word[word] = freq_word.get(word, 0)

#     sorted_data = sorted(
#         freq_word.items(), key=lambda item: item[1], reverse=True)

#     for key, val in sorted_data[:3]:

#         print(f"{key}: {val}")


# with open("C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "r") as f:
#     content = f.read()
#     words = content.split()
#     freq_words = {}

#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         freq_words[word] = freq_words.get(word, 0) + 1

#     sorted_words = sorted(freq_words.items(),
#                           key=lambda item: item[1], reverse=True)

#     for key, val in sorted_words[:3]:
#         print(f"word {key} : count : {val}")


# with open("C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "r") as f:
#     content = f.read()
#     words = content.split()
#     f_words = {}
#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         if word in f_words:
#             f_words[word] = f_words[word] + 1
#         else:
#             f_words[word] = 1

#     sorted_list = sorted(
#         f_words.items(), key=lambda item: item[1], reverse=True)

#     for key, val in sorted_list[:3]:
#         print(f"{key} : {val}")


# with open("C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "r") as f:
#     content = f.read()
#     words = content.split()
#     freq_words = {}
#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         if word in freq_words:
#             freq_words[word] = freq_words[word] + 1
#         else:
#             freq_words[word] = 1

#     s_list = sorted(freq_words.items(), key=lambda item: item[1], reverse=True)
#     for key, val in s_list[:3]:
#         print(f"{key} , {val} ")


with open("C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt", "r") as f:
    content = f.read()
    words = content.split()
    freq_words = {}
    for word in words:
        if word in freq_words:
            freq_words[word] = freq_words[word] + 1
        else:
            freq_words[word] = 1

    sorted = sorted(freq_words.items(),
                    key=lambda item: item[1], reverse=True)

    for key, val in sorted[:3]:
        print(f"{key} : {val}")
