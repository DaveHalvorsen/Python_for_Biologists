# This program is called DNA_translation.py and it is an exercise from the chapter 8: 
# Dictionaries chapter from the book Python for Biologists. The exercise is to write
# a program that will translate a DNA sequence into a protein. It needs to: split the
# DNA sequence into codons, look up the amino acid residue for each codon, and then
# join all the amino acids to give a protein.

# This is the dictionary for genetic code. The keys are codons and the values are amino
# acid residues. It was supposed to be provided in the Chapter_8 exercise folder as a file 
# called genetic_code.txt, but I couldn't find it there. I copied it from a file called 
# gencode.py in the Chapter_8 examples folder.
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

# dna = "ATGTTCGGTATTXXX" 
# This is a short sequence to test out the program on a scale that I can check by hand.
# Note the 'XXX' at the end of the input. It is not in the dictionary, to test a part
# of the program that handles entries that are not in the dictionary. 

# dna = "ATGTTCGGTA"
# This dna input has 10 characters, so it is not divisible by 3 (the last set of 1 or 2
# letters will not match up in the dictionary.) There's a if/else statement in the program
# that takes care of this potential issue, but I have it blocked out because the current
# iteration of the code deals with 'XXX', which is not in the dictionary.

def DNA_translation(dna):
    # last_i is part of the for i iteration that is the only for loop in this code.
    last_i = 0
    # This empty string is what we add the amino acids to.
    protein = ""
    # This part of the code checks if the input sequence is a multiple of 3. If it's a 
    # multiple of three, then the range of the translation continues on another 3 ...
    # it's starting point is 3, not 0. This code isn't as readable as it could be.
    # The else keeps the range down to the last multiple of three in the codon.
    if len(dna) % 3 == 0:
        range_end = len(dna) + 3
    else: 
        range_end = len(dna)
    # This for loop iterates through the entire range of the dna IF it's a multiple of 3
    # (see above). If it's not a multiple of three, then the code stops at the last multiple
    # of 3. There are lots of print statements in the for loop and each of them is for 
    # diagnostic purposes, so ignore those cause the program works now. 
    for i in range (3, range_end, 3):
        # print ("Current i is: " + str(i))
        # The dictionary doesn't seem to work with inputs of list slicing, so I've made
        # this variable as the input for the dictionary check.
        current_codon = dna[last_i:i]
        # print ("Current codon is: " + current_codon)
        # If a nonsensical codon is entered, it won't be found in the dictionary. That's why
        # this if/else statement prefaces the dictionary lookup. If the current_codon is in
        # the dictionary, then the codon is looked up in the dictionary and added to the 
        # protein string. If it's not in the dictionary, then 'N' is added to the string
        # 'N' means any potential codon was inputted there. 
        if current_codon in gencode:
            # print("Current amino acid is: " + gencode[current_codon])
            protein = protein + gencode[current_codon]
        else:
            # print("Current amino acid is: 'X'")
            protein = protein + 'X'
        # This keeps track of the last_i, so it can be the start of the list slice for
        # an input to the dictionary.
        last_i = i
    # This is a remnant of back when I was using print to check the right output. The only remaining
    # bit of code is the return function. Also, when I started the program wasn't encapsulated as a
    # function, so the print was more useful.    
    # print("The final protein string is: " + protein)
    return protein
# This call contains an unknown codon, so it's output should be 'X'
print(DNA_translation("ATGTTCGGTATTXXX"))
# This call's codons are not divisible by 3, so the output should stop after the 9th nucleotide
print(DNA_translation("ATGTTCGGTA"))


# These assertions test the programs output to match the expected output for their entires.
assert(DNA_translation("ATGTTCGGT")) == "MFG"
assert(DNA_translation("ATCGATCGAT")) == "IDR"
assert(DNA_translation("ACGANCGAT")) == "TXD"



