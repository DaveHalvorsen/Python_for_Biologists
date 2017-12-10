# This program is called Accession_names.py. It is part of the Regular Expressions chapter from the book
# Python for Biologists. There are 9 different challenges involving regular expressions. You can see
# each individual challenge by goingh through the program and finding each "#". Those are the separators
# for each requirement.
# Regular expressions aren't natively part of Python, so they must be imported from the 're' module.
import re
# accs is the provided list from the textbook of the strings to run regular expressions on. Note that
# every time the 're' module is used that the tool has to be prefixed by the 're.'
accs = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
# contains 5
# re.search is a true/false function that determines whether or not the pattern appears somewhere in 
# the string. Its two arguments are the pattern that is being searched for and the 2nd is the string
# to search within. Regular expressions require the usage of special characters that would otherwise
# trigger special functions in Python. The search patter must be prefaced with r before the quotations
# to indicate raw input, so special characters that ARE NOT associated with regular expressions are 
# ignored. The contains 5 test is simple and only has "5", BUT it does get harder. 
print("Contains 5: ")
for acc in accs:
    if re.search(r"5", acc):
        print("\t" + acc)
# contains the letter d or e
# The pipe operator is used to signify or here.
print("Contains the letter 'd' or 'e': ")
for acc in accs:
    if re.search(r"d|e", acc):
        print("\t" + acc)
# contains the letters d and e in that order
# The period indicates that any character type can go after the 'd' and the asterisk allows anywhere 
# from 0 - N characters before an 'e' is found. 
print("Contains the letters 'd' and 'e' in that order: ")
for acc in accs:
    if re.search(r"d.*e", acc):
        print("\t" + acc)
# contains the letters d and e in that order with a single letter between them
# The period allows any SINGLE character to go between the 'd' and 'e' characters. 
print("Contains the letters 'd' and 'e' with a single character between them: ")
for acc in accs:
    if re.search(r"d.e", acc):
        print("\t" + acc)
# contains both the letters d and e in any order
# This is essentially the same as an earlier exercise, BUT now the order doesn't matter.
# The code is repeated from above, BUT with "or" between the reversed options. 
print("Contains both the letters 'd' and 'e' in any order: ")
for acc in accs:
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc):
        print("\t" + acc)
# starts with x or y
# The '^' caret character doesn't allow any characters to go first, EXCEPT for either 
# 'x' or 'y'
print("Starts with 'x' or 'y': ")
for acc in accs:
    if re.search(r"^(x|y)", acc):
        print("\t" + acc)
# starts with x or y and ends with e
# This code is the same as the directly previous exercise, but with the addition of a
# period and then an asterisk to mean that any character type can happen 0 - N times
# before ending with 'e'. The dollar sign after 'e' indicates that it must be the last
# item of the string. 
print("Starts with 'x' or 'y' and ends with 'e': ")
for acc in accs:
    if re.search(r"^(x|y).*e$", acc):
        print("\t" + acc)
# contains three or more digits in a row
# \d allows any character of the set 0-9. Curly brackets with a number followed by a comma
# mean that the previous pattern is repeated 3 times. 
print("Contains three or more digits in a row: ")
for acc in accs:
    if re.search(r"\d{3,}", acc):
        print("\t" + acc)
# ends with d followed by either a , r, or p
# d is the first character in the pattern. Brackets are used around 'arp' to allow for any of
# the three characters to happen. The dollar sign means that the preceding pattern is what the
# string must end on for the search to pass as true. 
print("Ends with 'd' followed by either 'a', 'r', or 'p': ")
for acc in accs:
    if re.search(r"d[arp]$", acc):
        print("\t" + acc)
