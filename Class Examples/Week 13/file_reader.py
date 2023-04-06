
def binary_search(key, name_list, reverse=False):
    # --- Binary search


    lower_bound = 0
    upper_bound = len(name_list)-1
    found = False

    # Loop until we find the item, or our upper/lower bounds meet
    condition = lower_bound <= upper_bound and not found
    if reverse:
        condition = lower_bound >= upper_bound and not found

    while condition:
        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2

        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

        condition = lower_bound <= upper_bound and not found
        if reverse:
            condition = lower_bound >= upper_bound and not found

    if found:
        print( "The name is at position", middle_pos)
    else:
        print( "The name was not in the list." )

def reverse_sort_the_list(name_list):
    reverse_list = name_list.copy()
    reverse_list.sort(reverse=True)
    return reverse_list

def linear_search(key, name_list):
    # --- Linear search

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        # Advance to the next item in the list
        current_list_position += 1

    if current_list_position < len(name_list):
        print("The name is at position", current_list_position)
    else:
        print("The name was not in the list.")



def read_into_list():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    # Create an empty list to store our names
    name_list = []

    # or
    # my_file.readlines()

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        name_list.append(line)

    my_file.close()

    print("There were", len(name_list), "names in the file.")
    return name_list

def a_better_close():
    """ Read in lines from a file """

    # Open file, and automatically close when we exit this block.
    with open("super_villains.txt") as my_file:
        # Loop through each line in the file like a list
        for line in my_file:
            line = line.strip()
            print(line)

def close_the_file():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    # Loop through each line in the file like a list
    for line in my_file:
        line = line.strip()
        print(line)

    my_file.close()

def remove_blank_lines():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    # Loop through each line in the file like a list
    for line in my_file:
        line = line.strip()
        print(line)

def simple_read():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    # Loop through each line in the file like a list
    for line in my_file:
        line = line.strip()
        print(line)

def main():
    simple_read()
    remove_blank_lines()
    close_the_file()
    a_better_close()
    villains = read_into_list()
    linear_search("Astarte Hellebore", villains)
    reverse_villains = reverse_sort_the_list(villains)
    #print(reverse_villains)
    linear_search("Astarte Hellebore", reverse_villains)
    binary_search("Astarte Hellebore", reverse_villains, reverse=True)
    binary_search("Astarte Hellebore", villains)

main()
