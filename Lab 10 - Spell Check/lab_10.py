import re

# This function takes in a line of text and returns
# a list of words in the line.


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    my_file = open("dictionary.txt")
    dictionary_list = []
    for entry in my_file:
        entry = entry.strip()
        dictionary_list.append(entry)
    my_file.close()
    current_list_position = 0
    print("---Linear Search---")
    # --- Linear search
    key = open("AliceInWonderLand200.txt.")
    word_list = []
    for line in key:
        word_list = split_line(line)
        for word in word_list:
            current_list_position += 1
            if word not in dictionary_list:
                print("Line:", current_list_position, word, "could be spelled incorrectly")
    key.close()
    print("---Binary Search---")
    key = open("AliceInWonderLand200.txt.")
    word_list = []
    """for line in key:
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(word_list) - 1
            found = True
            while lower_bound <= upper_bound and found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] in dictionary_list:
                    lower_bound = middle_pos + 1
                if dictionary_list[middle_pos] in dictionary_list:
                    upper_bound = middle_pos - 1
                else:
                    found = False
            if found:
                print(word)
            else:
                print(word)""" # I couldn't figure it out



main()

