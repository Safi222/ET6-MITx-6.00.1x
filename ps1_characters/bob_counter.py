"""
A program that prints the number of times the string 'bob' occurs in s
"""

count = 0
name = "bob"
s = input("Enter a name: ").lower()
for i in range(len(s)):
    if s[i]=="b" and s[i+1]=="o" and s[i+2]=="b":
        count += 1
        
print("Number of times bob occurs is:", count)