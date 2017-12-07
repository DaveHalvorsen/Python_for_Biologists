#This program is called Length_range.py. It is part of the Conditional tests
#chapter from the book Python for Biologists. This program accesses the file called
#data.csv and prints out the gene names for all the genes between 90 and 100 
# bases long

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
    #If the length of the second element [1], the gene sequence, is >=90 and <=110,
    #then the gene name

    if len(split_line[1]) >= 90 and len(split_line[1]) <= 110:
        print ("The gene name is " + (split_line[2]) )
