# Python code to convert binary number
# into hexadecimal number

# function to convert
# binary to hexadecimal

def hex_number(number):
    int_number = int(number, 16)
    number_converter(number, int_number)

def binary_number(number):
    int_number = int(number, 2)
    number_converter(number, int_number)

def number_converter(original, int_number):
    print(original, "in decimal is :", int_number)
    print(original, "in binary is : ", bin(int_number))
    print(original, "in hexadecimal is : ", hex(int_number))
    print(original, "in octal is : ", oct(int_number))

while True:
    try:
        choice = input('Enter number type to convert (d decimal, b binary, h hexadecimal, or q to quit followed by enter): ')
        if choice == 'q':
            break
        elif choice == 'd':
            number = input('Enter decimal number: ')
            number_converter(number, int(number))
        elif choice == 'h':
            number = input('Enter hexadecimal number: ')
            hex_number(number)
        elif choice == 'b':
            number = input('Enter binary number: ')
            binary_number(number)
    except:
        print("Error in input, please make sure you using the correct format for digits.\n"
              "For binary, valid digits are 0 and 1. For decimal valid digits are 0-9. \n"
              "For hexadecimal valid digits are 0-9 and A-F.")


