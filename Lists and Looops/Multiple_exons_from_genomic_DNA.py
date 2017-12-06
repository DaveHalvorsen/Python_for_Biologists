#This program is called "Multiple_exons_from_genomic_DNA.py." It is part of
#the lists and loops chapter of the Biology and Python book. This program
#accepts input from two files. An exons.txt contains the start and stop
#positions for the exons in a coding region. File genomic_dna.txt contains
#the genomic dna sequence. The program identifies the coding regions of the
#provided genomic DNA sequence and stores them in a new file called 
#coding_regions.txt.
#Here the exons list and the genomic dna files are opened for being used.
my_file_name = open("exons.txt")
all_lines = my_file_name.readlines()
dna_file = open("genomic_dna.txt")
my_dna = dna_file.read()
#There's a iterator in the for loop that is started at 1 here.
i = 1
#I use a dictionary for the genomic_sequence that is currently identified by
#the provided exon start and stop position within the loop. It's not required
#to do a dictionary because each iteration's i is all that's required, BUT I
#wanted to have practice on working with this data structure. 
genomic_sequence = dict()
#Each cycle of the iterator adds the currently identified coding region to the
#variable concatendated_exons. Here it's defined as an empty string. 
concatenated_exons = ""
#This for loop cycles through the provided start and stop positions from the exons
#list and concatenates the determined coding region for each iteration. It cycles
#through every line in the exon.txt file. 
for line in all_lines:
    #These print statements were used for diagnostics early on in creation of the 
    #program. I use .rstrip("\n") on the print command because I didn't want spaces.
    #Note that I'm not changing the line here ... it's just a cosmetic issue. 
    print("line INITIALLY: " + str(line).rstrip("\n"))
    print("i is currently: " + str(i))
    #The exon positions for each line are split by commas, BUT I need to have the start
    #and stop positions in a [start:stop] format, so I break the current line up on the
    #commas into a list. The left and right variables store the start and stop positions
    #by using character locators within the string to get the 0th position or the 1th 
    #position. Note that .rstrip("\n") is used here to change the data because otherwise
    #that new line character would be passed into the line slicing. #In hindsight, start
    #and stop names for the variables would be a better choice for explanatory power. 
    line = line.split(",")
    left = line[0]
    right = line[1].rstrip("\n")
    print("left is " + left)
    print("right is " + right)
    #Here the genomic_sequence[i] dictionary is being passed start and stop positions for
    #it's slicing. A translation into int is required because it's being passed a string. 
    #This is where care is required is picking the right slice locations. Recall the differences
    #between how python counts characters and how humans normally count characters:
    #Coding Positions: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    #Normal Character: 1 2 3 4 5 6 7 8 910 11 12 13 14 15 16
    #A human designated start position of 5 requires using a python location of 4 as the start
    #index is inclusive. Therefore, all starting slice positions need a "-1" to be accurate.
    #Recall that the end position is exclusive, so a human-designated end position of 10 requires
    #an end slice of 9, BUT a +1 is required because the end of a slice is exclusive; this places
    #the stop position back at where it would naturally be. This reasoning is why start slices 
    #get -1 and all end slice positions are unchanged.
    genomic_sequence[i] = my_dna[(int(left)-1):int(right)]
    #This print statement is purely for diagnostic purposes. 
    print("The coding region for exon " + str(i) + " is " + genomic_sequence[i])
    #This concatenates the currently identified coding regions with the previously identified
    #coding regions. The print statement is for diagnostic purposes. The i is +=1 to prepare
    #for the next iteration. i isn't necessary for the program and the dictionary could be
    #removed for a simpler program, but this is all for practice with dictionaries. 
    concatenated_exons = concatenated_exons + genomic_sequence[i]
    print("Concatenated exons are currently: " + concatenated_exons)
    i += 1
#This opens a new file that the concatenated coding regions is stored within. 
new_file = open("coding_regions.txt", "w")
new_file.write(concatenated_exons)
#Here, the three files that were worked on are closed.
dna_file.close()
my_file_name.close()
new_file.close()
