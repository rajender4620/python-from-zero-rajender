# with open('C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt', 'r') as f:
#     content = f.read()
#     words = content.split()
#     freq_words = {}
#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         if word in freq_words:
#             freq_words[word] = freq_words[word] + 1
#         else:
#             freq_words[word] = 1

#     sorted_words = sorted(freq_words.items(),
#                           key=lambda item: item[1])

#     for key, val in sorted_words[:5]:
#         print(f"{key} : {val}")


"""2. Word Length Count
Instead of frequency, count how many words have each length.

Example:

txt
Copy
Edit
"Hello there good sir"
Output:

yaml
Copy
Edit
5-letter words: 2
4-letter words: 1
3-letter words: 1"""

# with open('C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt', 'r') as f:
#     content = f.read()
#     print(content)
#     words = content.split()
#     count_words = {}
#     count = 0
#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         word_length = len(word)
#         if word_length in count_words:
#             count_words[word_length] = count_words[word_length] + 1
#         else:
#             count_words[word_length] = 1
#     sorting = sorted(count_words.items())

#     for key, val in sorting:
#         print(f"{key}-letter words : {val}")


# """3. Longest Word(s)
# Find and print the longest word(s) in the text. If there are multiple, show all."""

# with open('C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt', 'r') as f:
#     content = f.read()
#     print(content)
#     words = content.split()
#     largest_words = []
#     max_len = 0
#     for word in words:
#         word = word.lower().strip('.,!?\"\'')
#         word_length = len(word)

#         if word_length > max_len:
#             largest_words = [word]
#             max_len = word_length
#         elif word_length == max_len:
#             largest_words.append(word)

#     print(largest_words)


"""Map each word to the line numbers where it appears in the file."""


import string
with open('C:/python-from-zero-rajender/day09_read_and_write_flies/quotes.txt', 'r') as f:
    content = f.readlines()
    print(content)

    # for line in content:
    #     print(line)

    #  to get the index i will use enumareate
    map_word: dict[str, list[int]] = {}
    count = 1
    for index, line in enumerate(content):
        line_num = index + 1
        words = line.strip().split()
        cleaned_words = [w.lower().strip('.,!?\"\'') for w in words]
        unique_words = set(cleaned_words)

        for word in unique_words:
            if word not in map_word:
                map_word[word] = [line_num]
            else:
                map_word[word].append(line_num)

    print(map_word)
