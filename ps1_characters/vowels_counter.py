"""
    program that counts up the number of vowels
    contained in the string s.
    Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
"""

count = 0
vowels = "aeiou"
s  = input("Enter a string: ").lower()
for i in range(len(s)):
    if s[i] in set(vowels):
        count += 1

print("Number of vowels:", count)