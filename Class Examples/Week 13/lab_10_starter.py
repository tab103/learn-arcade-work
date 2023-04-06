import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    # read dictionary into a list

    # read chapter into a list of lines

    # close both

    # linear search
    print('--- Linear Search ---')

    # recommend writing in a function

    # read chapter one line at a time
    # for each line call split line
    # for each word in line, convert to upper and check for presence in dictionary
    # if it is NOT found, print the word and the line number as in:
    # Line x possible misspelled word: word

    # binary search
    print('--- Binary Search ---')



