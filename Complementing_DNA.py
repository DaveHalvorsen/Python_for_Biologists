#This program takes in a provided DNA sequence and returns its complement.
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
my_dna_lower = my_dna
#There are 4 transitions required: A to T, T to A, G to C and C to G.
#That can't be done properly without protecting each newly transitioned
#nucleotide from future transitions, so I replace each nucleotide with
#a lower case version of it's complement. 
my_dna_lower = my_dna_lower.replace('A', 't')
my_dna_lower = my_dna_lower.replace('T', 'a')
my_dna_lower = my_dna_lower.replace('G', 'c')
my_dna_lower = my_dna_lower.replace('C', 'g')
my_dna_upper = my_dna_lower.upper()
print("The provided DNA sequence is: " + my_dna)
print("The complement of that DNA sequence is: ")
print(my_dna_upper)

