import re


# This function takes in a line of text and returns
# a list of words in the line.
# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall("[A-Za-z]+(?:'[A-Za-z]+)?", line)


# creates a list
dictionary_list = []
# variable holds the open file
dictionary_file = open("dictionary.txt")
# for line in file
for line in dictionary_file:
    line = line.strip()
    # takes out space
    # list adds the value of(line) from the file
    dictionary_list.append(line)
# closes the file
dictionary_file.close()

print("--- Linear Search ---")


def linear_search():
    # variable holds the open file
    alice_file = open("AliceInWonderLand200.txt")
    # where the line number starts
    line_num = 0
    # for line in file
    for line in alice_file:
        # add one to the line_num
        line_num += 1
        # variable holds the value of split lines from file
        word_list = split_line(line)
        # for word in list
        for word in word_list:
            # current position
            i = 0
            # while current position is less than the length of list and word is equal to the current position
            while i < len(dictionary_list) and word.upper() != dictionary_list[i]:
                # add one to the current position
                i += 1
            # breaks out the code when condition fails
            # if current position equals the length of list
            if i == len(dictionary_list):
                print("Line", line_num, "possible misspelled word:", word)
    # closes the file
    alice_file.close()


# calls function
linear_search()

print("--- Binary Search ---")


def binary_search():
    # variable stores open file
    alice_file = open("AliceInWonderLand200.txt")
    # where the line number starts
    line_num = 0
    # for line in file
    for line in alice_file:
        # add one to line number
        line_num += 1
        # variable holds the value of split lines from file
        word_list = split_line(line)
        # for word in list
        for word in word_list:
            lower_position = 0
            upper_position = len(dictionary_list) - 1
            # the word has not been found, so carry out code below
            word_found = False
            # while loop continues until condition is met
            # while the lower_pos is less than or equal to upper_pos and word is not found
            while lower_position <= upper_position and not word_found:
                # middle_poss equals lower_pos and upper_pos floor div 2
                middle_pos = (lower_position + upper_position) // 2
                # if the list's middle_pos is less than word
                if dictionary_list[middle_pos] < word.upper():
                    # then lower_pos equals middle_poss plus one
                    lower_position = middle_pos + 1
                # if list's middle_pos is greater than word
                elif dictionary_list[middle_pos] > word.upper():
                    # then upper_pos equals middle_pos minus 1
                    upper_position = middle_pos - 1
                # else dictionary_list[middle_pos] equals word
                else:
                    # word is found
                    word_found = True
            # breaks out the loop into this condition after it fails
            if not word_found:
                print("Line", line_num, "possible misspelled word:", word)
    # closes the file
    alice_file.close()


# calls function
binary_search()
