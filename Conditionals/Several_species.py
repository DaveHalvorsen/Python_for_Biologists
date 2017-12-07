#This program is called Several_species.py. It is part of the Conditional tests
#chapter from the book Python for Biologists. This program accesses the file called
#data.csv and prints out the names for all the genes belonging to 
#Drosophila melanogaster.

#First the data.csv file is opened and stored in a variable called all_lines that
#can be used to cycle through with a for loop.
data_file = open("data.csv")
all_lines = data_file.readlines()

#This for loop cycles through each line in the provided all_lines variable. 
for line in all_lines:
    #I've never worked with CSV files before, so I wanted to determine the type of data
    #I was working with, so here's that remnant that initially helped me.
    #print (type(line))
    #The program needs to output single elements of the string, so I broke up the string
    #into a list that the program can grab individual elements of. 
    split_line = line.split(',')
    #If the first element of the split_line list of strings starts with the name of the 
    #organism that is being searched for, the list's third element [2] will be printed.
    #The csv file doesn't have a header, so I assumed that the third elements were the genes
    #because nothing else seemed to fit the required description. 
    if split_line[0].startswith('Drosophila melanogaster') or split_line[0].startswith('Drosophila simulans'):
        print ("One gene name for " + split_line[0] + " is " + split_line[2])

    
    
