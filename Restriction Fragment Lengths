#The book Python for Biologists claims to teach scientists programming.
#This is my solution to the Chapter 2 exercise: Restriction fragment lengths.
#The exercise asks to calculate the length of the two sequences after EcoRI cuts my_dna.
#Molecular machines, called restriction enzymes, can cut DNA strings at known nucleotide sequence sites.
#EcoRI cuts at sites with the sequence "GAATTC." It cuts between the G and the first A.
#The asterisk is where it cuts: "G*AATTC."

#my_dna is the provided sequence. We learn about working with files in the next chapter.
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#First, I use the find method to determine the start for the restriction enzyme site. 
#Recall that Python starts out strings with position 0, whereas I typically use 1 to start a string.
#Python will find "GAATTC" to have an index of 21, whereas I'd consider it 22 (I counted the string.)
cut_site_start = my_dna.find("GAATTC")

#The left length is 22. Python's index sees that EcoRI initiation site as 21 because index is 0.
#Index 0 -> 1 is why I need to add 1 to the find method's EcoRI site location.
left_length = cut_site_start + 1

#The right side's length is just the total length minus the left side's length.
tot_length = len(my_dna)
right_length = tot_length - left_length

#Now, all we need to do is print the lengths of each fragment!
print("The length of fragment 1 is: " + str(left_length))
print("The length of fragment 2 is: " + str(right_length))
