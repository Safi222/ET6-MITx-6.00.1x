"""
A program that prints the longest substring of s in which the letters occur in alphabetical order.
"""

string = ""
s = input("Enter a string: ")
longest_string = ""
for i in range(0, len(s)):
    if s[i] >= s[i-1]: 
        string += s[i]
    else:
        if len(string) > len(longest_string):
            longest_string = string
        string = s[i]

if len(string) > len(longest_string):
    longest_string = string

print("Longest substring in alphabetical order is:", longest_string)