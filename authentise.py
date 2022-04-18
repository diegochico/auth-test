"""This program takes a user input string from command line and reverse its characters"""


# Function to get the user input
def get_input(text):
    return input(text)


# Function to reverse words of string
def reverse_letters():
    in_text = get_input("Enter your word: ")
    output = in_text[::-1]
    return output


print(reverse_letters())
