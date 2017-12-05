#This program creates three FASTA files and adds DNA sequences to them.
#The w+ functionality is used, so that files can be created and written. 
ABC = open("ABC123.fasta", "w+")
DEF = open("DEF456.fasta", "w+")
HIJ = open("HIJ789.fasta", "w+")

#This is the input that the exercise calls for (both headers & DNA sequences): 
ABC_header = "ABC123"
ABC_DNA_sequence = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
DEF_header = "DEF456"
DEF_DNA_sequence = "actgatcgacgatcgatcgatcacgact"
HIJ_header = "HIJ789"
HIJ_DNA_sequence = "ACTGCA-ACTGT--ACTGTA----CATGTC"

#These are the write commands that add the required text. ">" is appended to the start
#of the file, followed by the required header. A new line is created (to print on the
# next line) and then the required DNA sequence is printed. .upper is used to make 
#sure that everything is upper case. .replace is used to remove all of the hyphens from 
#the HIJ789 file. I initially tried using rstrip, but that only works for items on the
#outside of a text string, so replace is required. 
ABC.write(">" + ABC_header + "\n" + ABC_DNA_sequence.replace("-", "").upper())
DEF.write(">" + DEF_header + "\n" + DEF_DNA_sequence.replace("-", "").upper())
HIJ.write(">" + HIJ_header + "\n" + HIJ_DNA_sequence.replace("-", "").upper())

#Now all the files that were worked on are closed. 
ABC.close()
DEF.close()
HIJ.close()
