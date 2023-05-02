# Imports regular expressions
import re


# This function takes a line of text and returns
# a list of words in the line


def split_line(line):
    split = re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
    return split


# Opens the dictionary text file and adds each line to an array, then closes the file
dictionary = open("dictionary.txt")
dictionary_list = []

for item in dictionary:
    item = item.strip()  # strips off carriage returns
    dictionary_list.append(item)
# print(dictionary_list)
dictionary.close()

print("---Linear Search---")

# Opens the text for the first chapter of Alice in Wonderland
chapter_1 = open("AliceInWonderland200.txt")

# Breaks down the text by line
line_num = 0
for each_line in chapter_1:
    line_num += 1
    # Breaks down each line to a single word
    word_list = split_line(each_line)
    # Checks each word against the dictionary array
    for each_word in word_list:
        i = 0  # initialize to zero
        # check dictionary list comparing each word to the curry word being search for
        while i < len(dictionary_list) and dictionary_list[i] != each_word.upper():
            i += 1

        if i == len(dictionary_list):
            print(each_word, 'possibly misspelled at line', line_num)

# Closes the first chapter file
chapter_1.close()

print("--- Binary Search ---")

chapter_1 = open("AliceInWonderland200.txt")
for each_line in chapter_1:
    line_num += 1
    # Breaks down each line to a single word
    word_list = split_line(each_line)
    for each_word in word_list:
        lower_bound = 0
        upper_bound = len(dictionary_list) - 1
        found = False
        while lower_bound <= upper_bound and not found:
            middle_position = (lower_bound + upper_bound) // 2

            # figure out if we need to move up or down
            if dictionary_list[middle_position] < each_word.upper():
                lower_bound = middle_position + 1
            elif dictionary_list[middle_position] > each_word.upper():
                upper_bound = middle_position - 1
            else:
                found = True
        if not found:
            print(each_word, "possibly misspelled word at line", line_num)

chapter_1.close()
