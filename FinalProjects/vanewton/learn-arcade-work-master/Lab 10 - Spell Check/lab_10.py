import re

def split_line(line):
    return re.findall('[A-Za-z]+ (?:\'[A-Za-z]+)?',line)

def main():
    my_file = open("AliceInWonderLand200.txt")
    name_list = []

    for line in my_file:
        line = line.strip()

        name_list.append(line)

    my_file.close()

    print("There were",len(my_file),"names in the file.")










main()