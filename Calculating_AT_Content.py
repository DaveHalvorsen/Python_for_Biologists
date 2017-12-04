#This program will print out the AT content of the provided DNA sequence.
#I use the count methods to determine the number of As and Ts.
#The len function is used to determine total dna length.
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_count = my_dna.count('A')
T_count = my_dna.count('T')
Total_length = len(my_dna)
#AT content is the percentage of A and T QUANTITY divided by the total length.
AT_content = 100 * (A_count + T_count)/Total_length
#This limits the number to having two decimal points. 
AT_content = str(round(AT_content, 2))
print("The provided DNA sequence is: " + my_dna)
print("The AT content is: " + AT_content + "%.")
