#This program is called Percentage_of_amino_acid_residues_1.py. It is part of 
#the Functions chapter of the Python for Biologists book. This program takes
#inputs of an amino acid residue and a protein string. The program returns
#the percentage of the amino acid residue in the protein string. This is
#my first introduction to using assertions to test the function. Those are at
#the end of the program.

#This is the amino acid percentage calculator program.
def percent_amino_acid(protein_seq, AA_code):
    #The length is used to divide the amino acid count by.
    protein_length = len(protein_seq)
    #Both sequences need to be in the same case so that they can be compared.
    #I've used upper here arbitrarily. It would have worked just as well with lower.
    AA_code_upper = AA_code.upper()
    protein_seq_upper = protein_seq.upper()
    #This is the count of amino acid residues in the protein sequence. It's divided by
    #the total protein length. The returned output included 1 decimal point, so I was 
    #concerned that it would fail the assertion test. That's why I used an int() wrapping
    #to drop it to no decimal places, BUT I've discovered afterwards that it passes the
    #assertion test whether or not the int() is used. 
    AA_code_count = protein_seq_upper.count(AA_code_upper)
    AA_percent = int(100 * AA_code_count / protein_length)
    return AA_percent
#I've included these print statements because I wanted to see a visualized
#report of the inputs and outputs. The book makes the claim that assertion
#statements are provided in the website file download, BUT I couldn't find 
#the files. I was concerned that I might mistype the inputs from the text,
#so I tested the outputs before running the assertion tests.
print('The result of inputs of ("MSRSLLLRFLLFLLLLPPLP", "M") is: ')
print(percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", "M"))

print('The result of inputs of ("MSRSLLLRFLLFLLLLPPLP", "r") is: ')
print(percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", "r"))

print('The result of inputs of ("msrslllrfllfllllpplp", "L") is: ')
print(percent_amino_acid("msrslllrfllfllllpplp", "L"))

print('The result of inputs of ("MSRSLLLRFLLFLLLLPPLP", "Y") is: ')
print(percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", "Y"))

#Here are the assertion tests.
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert percent_amino_acid("msrslllrfllfllllpplp", "L") == 50
assert percent_amino_acid("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
