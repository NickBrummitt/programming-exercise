'''
Exercise Description: In this exercise, you will develop a function named 'decode(message_file)'. This function should
read an encoded message from a .txt file and return its decoded version as a string.

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the
arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order,
with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers
increase consistently, like so:

    1
   2 3
  4 5 6

The key to decoding the message is to use the words corresponding to the number at the end of each pyramid line (in
this example, 1, 3, and 6). You should ignore all the other words. So for the example input file, the message words are:

1: I
3: love
6: computers

and the function should return the string "I love computers"
'''


import re  # Import Regular Expression Library

message_file = open(input(), "r")  # Open and read input text file
lines = sorted(message_file.readlines())  # Sort the file numerically


# Function to perform numerical sort
def num_sort(x):
    return list(map(int, re.findall(r'\d+', x)))[0]


lines.sort(key=num_sort)  # Sort list numerically


def decoder(lines):
    phrase = ""  # Initialize phrase variable. This will be the output.
    row = 1  # Variable to track the row of data we are interating through
    i = 1  # Variable to pyramid scheme addition

    for n in lines:
        if (str(i) + " ") in n:
            pos = max(n.find(' '), n.find(' '), 0)  # Find the position where the word starts
            phrase += str(n[pos:len(n) - 1])  # Concatenate the phrase with the word found
            i += row + 1  # Increment 'i' counter
            row += 1  # Increment 'row' counter
            lines.remove(n)  # Remove line from list to make iteration faster
    return (phrase)


print(decoder(lines))  # Print results of the function
