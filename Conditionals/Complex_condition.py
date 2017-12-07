# This program is called Complex_condition.py. It is part of the Conditional tests
# chapter from the book Python for Biologists. This program accesses the file called
# data.csv and prints out the gene names for all the genes whose names begin with "k" 
# or "h" except those belonging to "Drosophila melanogaster."#

# First the data.csv file is opened and stored in a variable called all_lines that
# can be used to cycle through with a for loop.
data_file = open("data.csv")
all_lines = data_file.readlines()

# This for loop cycles through each line in the provided all_lines variable. 
for line in all_lines:
    # The program needs to output single elements of the string, so I broke up the string
    # into a list that the program can grab individual elements of. 
    split_line = line.split(',')
    # This is a complicated if statement that will print IF the gene starts starts with k or h 
    # and the organism name is not Drosophila melanogaster. First the third element of split_line
    # is checked for starting with k or h; all of that is within one parenthesis, so as to be as
    # clear as possible. Then, and not is used to check that the organism name is not 
    # Drosophila melanogaster.
    if (split_line[2].startswith('k' or 'h')) and not split_line[0] == "Drosophila melanogaster":
        print ("Gene name is: " + split_line[2] + " organism name is: " + split_line[0])
    
    
