#This program deteremines the length of two DNA strands after they are
#split by an EcoRI restriction enzyme.
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
total_length = len(my_dna)
#The find method is used to locate the start of the recognition site.
GAATTC_start = my_dna.find('GAATTC')
#The left sequence is determined by using list slciing to grab the start and
#finish sites. Recall that the end of the slice is exclusive, so + 1 is required. 
left_sequence = my_dna[0:(GAATTC_start + 1)]
#The len function is used to measure the length of the left side & the right length
#is determined by subtractin the total length by the length of the left side. 
left_length = len(left_sequence)
right_length = total_length - left_length
#I print the total length AND the additive length of the fragments as a way to check for
#an error in my code. 
print("The provided DNA sequence is: " + my_dna)
print("It's total length is: " + str(total_length))
print("That DNA is treated with the EcoRI restriction enzyme.")
print("Fragment 1 length is: " + str(left_length))
print("Fragment 2 length is: " + str(right_length))
Sum_frag_lengths = left_length + right_length
print("The length of fragment 1 + fragment 2 is: " + str(Sum_frag_lengths))

