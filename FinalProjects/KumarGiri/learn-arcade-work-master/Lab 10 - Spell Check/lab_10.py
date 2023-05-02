import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    # reading the dictionary.text file
    dictionary = open("Lab 10 - Spell Check\dictionary.txt")
    dictionary_word_list = []

    for word in dictionary:
        word = word.strip()
        dictionary_word_list.append(word)
    dictionary.close()

    # Linear Search code
    def linear_search():
        print("\n--- Linear Search ---")

        Alice = open("Lab 10 - Spell Check\AliceInWonderLand200.txt")

        # keeps track of line position in the text
        current_line_position = 0

        # looping throug each line
        for line in Alice:
            line =line.strip()
            word_list = split_line(line)
            current_line_position +=1

            # looping through every word
            for word in word_list:

                # to track dictionary word according to thier position
                current_d_word_position = 0

                # main linear search code 
                while current_d_word_position < len(dictionary_word_list) and dictionary_word_list[current_d_word_position]!=word.upper():
                    current_d_word_position += 1
                
                if current_d_word_position < len(dictionary_word_list):
                    continue
                else:
                    print(f"line {current_line_position} Possible error word: {word}")

        Alice.close()

        # Binary Search code
    def binary_search():

        print("\n--- Binary Search ---")

        Alice = open("Lab 10 - Spell Check\AliceInWonderLand200.txt")

        # keeps track of line position in the text
        current_line_position = 0

        # looping throug each line
        for line in Alice:
            line =line.strip()
            word_list = split_line(line)
            current_line_position +=1

        # looping through every word
            for word in word_list:

                lower_bound = 0
                upper_bound = len(dictionary_word_list)-1
                found = False

            # Loop until we find the item, or our upper/lower bounds meet
                while lower_bound <= upper_bound and not found:

            # Find the middle position
                    middle_pos = (lower_bound + upper_bound) // 2

                    if dictionary_word_list[middle_pos] < word.upper():
                        lower_bound = middle_pos + 1
                    elif dictionary_word_list[middle_pos] > word.upper():
                        upper_bound = middle_pos - 1
                    else:
                        found = True

                if found:
                    continue
                else:
                    print( f"line {current_line_position} Possible error word: {word}" )
        Alice.close()

    # to easily compare their speeed, I made into their own funtions, so you have less to comment in and out. 
    linear_search()
    binary_search()

main()

        



