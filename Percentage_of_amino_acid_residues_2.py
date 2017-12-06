#This program is called Percentage_of_amino_acid_residues_1.py. It is part of 
#the Functions chapter of the Python for Biologists book. This program takes
#inputs of an amino acid residue and a protein string. The program returns
#the percentage of the amino acid residue in the protein string. This is
#my first introduction to using assertions to test the function. Those are at
#the end of the program.

#This is the amino acid percentage calculator program. I have changed it from the 1st
#iteration to now have a for loop. It is now capable of checking for the number of
#amino acids EVEN if they're sent in as a list. As you can see, there's now a default
#input sequence that will run if no input is given. 
def percent_amino_acid(protein_seq, AA_code=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    #The length is used to divide the amino acid count by.
    protein_length = len(protein_seq)
    #I initially made the mistake of using the split on comma method because I thought
    #I'd need a string to iterate through, but I realized that a for loop can run
    #perfectly fine through a list. I've commented out that code as a reminder of my mistake. 
    #AA_code = AA_code.split(',').upper()
    #I've made the protein sequence upper case outside of the loop because it's a single
    #string. The amino acid sequence is made upper case within the for loop because
    #lists do not have an upper method. 
    protein_seq_upper = protein_seq.upper()
    #I use the count variable to count the number of hits of AA in the protein sequence 
    #within the for loop. 
    count = 0
    #This for loop cycles through each amino acid within the inputted amino acid list to 
    #count the number of times it matches the provided protein sequence. 
    for AA in AA_code:
        #The amino acid sequence is inputted as a list, so it doesn't have an upper function.
        #I call uper on it in the for loop because now it's just a single string item. I don't
        #necessarily need to call the upper method on it because the assertions don't have any
        #mismatched case, but I've decided to do so just in case a new kind of input might
        #happen in the future. 
        AA = AA.upper()
        #Ignore the three print commands within this loop. They were used for diagnostic purposes
        #early on in the generation of the program. 
        #print("The current AA is: " + AA)
        #This counts the number of times the current AA is within the protein sequence. 
        AA_code_count = protein_seq_upper.count(AA)
        #print("There are " + str(AA_code_count) + " of " + str(AA) + " in the protein sequence.")
        #This is an ongoing count that continues to be added to after each loop. 
        count = count + AA_code_count
        #print("The collective number of hits found so far is: " + str(count))
    #This calculates the percentage of times that the given amino acids are present within the
    #the provided protein sequence. 
    AA_percent = int(100 * count / protein_length) 
    print("The % of the amino acids in the protein sequence is: " + str(AA_percent))
    return AA_percent   
#These are assertions that test the functionality of the program.     
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", ["M", "L"]) == 55
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"]) == 70
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP") == 65

        

        

        
