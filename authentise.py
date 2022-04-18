#!/usr/bin/env python3

""" The program takes two arguments from the user input separated by space:
    First a quoted string (single or double)
    Second flags:
        -r: reversed the string character wise
        -w: reversed the string word wise
    example python authenthise.py "some text" -r
"""

import sys
import argparse
from os import path


class SmartFormatter(argparse.HelpFormatter):
    """Format the argparse help text to allow newlines insertion"""

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        return argparse.HelpFormatter._split_lines(self, text, width)


# Adding argparse to control the user input arguments
parser = argparse.ArgumentParser(description='This program reverse a quoted string',
                                 formatter_class=SmartFormatter)
# First argument
parser.add_argument('quoted string', type=str,
                    help='R|If the string provided is a existing path/filename,\n'
                         'the program will take the file name as input')
# Second argument
parser.add_argument('-r', '-w', action='store_true', required=True,
                    help='R|-r: reverse the string character wise\n'
                         '-w: reverse the string word wise')
parser.parse_args()


# Function to reverse words of string
def reverse_letters(in_text):
    output = in_text[::-1]
    return output


# Function to reverse string words wise
def reverse_words(in_text):
    # Splitting the string into words
    words = in_text.split(' ')
    # Reverse the list of strings and join them using space
    output = ' '.join(reversed(words))
    return output


def reverse_control(arguments):
    # Determines if the string is a file by its existence
    if path.isfile(arguments[0]):
        string_arg = path.basename(arguments[0])
    else:
        string_arg = arguments[0]
    # Choose the reverse function depending on the input
    if arguments[1] == '-r':
        output = reverse_letters(string_arg)
    else:
        output = reverse_words(string_arg)
    return output


if __name__ == '__main__':
    print(reverse_control(sys.argv[1:]))
