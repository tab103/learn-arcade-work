import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    dictionary_file = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    dictionary_file.close()

    # linear search
    def linear_search():
        print('--- Linear Search ---')
        alice_file = open("AliceInWonderLand200.txt")
        line_num = 0
        for line in alice_file:
            line_num += 1
            word_list = split_line(line)
            for word in word_list:
                i = 0
                found = False
                while i < len(dictionary_list) and not found:
                    if word.upper() == dictionary_list[i]:
                        found = True
                    i = i + 1
                if not found:
                    print("oh no! couldn't find",word,'in the dictionary! at line',line_num)


    # binary search
    def binary_search():

        print('--- Binary Search ---')
        alice_file = open("AliceInWonderLand200.txt")
        line_num = 0
        for line in alice_file:
            line_num += 1
            word_list = split_line(line)
            for word in word_list:

                lower_bound = 0
                upper_bound = len(dictionary_list) - 1
                found = False
                key = word

                # Loop until we find the item, or our upper/lower bounds meet
                while lower_bound <= upper_bound and not found:

                    # Find the middle position
                    middle_pos = (lower_bound + upper_bound) // 2

                    if dictionary_list[middle_pos] < key:
                        lower_bound = middle_pos + 1

                    elif dictionary_list[middle_pos] > key:
                        upper_bound = middle_pos - 1

                    else:
                        found = True
                    if found:
                        print(word, "is at position...", line_num)


    linear_search()
    binary_search()
main()
