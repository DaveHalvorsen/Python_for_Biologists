#This program is called "Splitting_Genomic_Data.py." It will open a file of DNA reads
#and then split that DNA up into coding and non-coding regions of DNA. It then writes
#those separate types of DNA into two different files.
#The open method directly below is how I'd do it for my computer, but I'm making this friendly
#for folks that open my Github page, so I'll stick with the open method that'll work for being
#in the same folder.
# my_file.open("C:\Users\David\Dropbox\Python for Biologists\exercises and examples\Chapter 3\exercises\genomic_data.txt")
my_file_name = "genomic_dna.txt"
my_file = open(my_file_name)
my_file_contents = my_file.read()
#The slicing structures I used below were originally for the Splicing_Out_Introns_1 exercise. 
#I've changed the variable that the slices act on, so that they cut up the genomic_data.txt
#file that I opened above.
exon1 = my_file_contents[0:63]
#The instructions state that the intron 1 starts at the 64th character and runs to the 90th character.
#Subtracting 1 from the chracter positions results in the slicing positions. 
intron1 = my_file_contents[63:90]
#The instructions state that exon 2 starts at CHARAcTER 91 and goes to the end of the sequence.
#The same -1 slicing rules apply AND recall that, to go to end of sequence, leave the end slice blank. 
exon2 = my_file_contents[90: ]
#Here the introns and exons are givens the "introns" and "exons" file names and the exon1 & 2
#are concatenated into a single variable called exons.
introns_to_save = intron1
exons_to_save = exon1 + exon2
#This creates the two text files that we'll be saving to: coding_dna & noncoding_dna
introns = open("non_coding_dna.txt", "w+")
exons = open("coding_dna.txt", "w+")
#These two lines save the introns and exons to the noncoding and coding dna.txt files from above. 
introns.write(introns_to_save)
exons.write(exons_to_save)
#This closes the three text files that were opened throughout the program. 
my_file.close()
introns.close()
exons.close()
