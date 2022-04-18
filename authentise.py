"""This program takes a user input string from command line and reverse its characters"""


# Function to reverse words of string
def reverse_letters(in_text):
    output = in_text[::-1]
    return output


string = 'qwerty uiop'
print(reverse_letters(string))

"""This program takes a user input string from command line and reverse its words"""


# Function to reverse string words wise
def reverse_words(in_text):
    # Splitting the string into words
    words = in_text.split(' ')
    # Reverse the list of strings and join them using space
    output = ' '.join(reversed(words))
    return output


string = 'writing something to reverse it'
print(reverse_words(string))
