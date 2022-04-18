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

"""This program takes a user input string from command line and reverse its words"""


# Function to reverse string words wise
def reverse_words():
    in_text = get_input("Enter your phrase: ")
    # Splitting the string into words
    words = in_text.split(' ')
    # Reverse the list of strings and join them using space
    output = ' '.join(reversed(words))
    return output


print(reverse_words())
