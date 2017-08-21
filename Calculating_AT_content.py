#The book Python for Biologists claims to teach scientists programming.
#This is my solution to the Chapter 2 exercise: Calculating AT content.
#This program calculates the AT content of the submitted string.
#In this case, I calculate AT content for the submitted string "my_dna."

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#AT content is the % of a given string that contains A or T.
#First I determine the individual A & T content of the string with the .count method.
A_content = my_dna.count('A')
T_content = my_dna.count('T')

#I need to determine the total length of the DNA string for the % calculation.
#Here I determine the total length with the len()argument.
DNA_length = len(my_dna)

#AT content is the quantity (# As + # Ts)/ DNAlength. 
#The parenthesis around the A & T content keeps order of operations.
AT_content = (A_content + T_content)/DNA_length

#I use the print command to output a standard string.
#The calculated AT_content *AFTER* it's converted from a # to a string.
print("The AT content is: " + str(AT_content))
