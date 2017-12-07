#This program is called AT_content.py. It is part of the Conditional tests
#chapter from the book Python for Biologists. This program accesses the file called
#data.csv and prints out the gene names for all the genes that have an AT content LESS
#than 0.5 AND whose expression level is GREATER than 200.

#First the data.csv file is opened and stored in a variable called all_lines that
#can be used to cycle through with a for loop.
data_file = open("data.csv")
all_lines = data_file.readlines()

#This AT_content was one of the original exercises. It has been turned in to a definition to
#be called upon within the upcoming for loop.
def AT_content(gene):
    A_count = gene.upper().count('A')
    T_count = gene.upper().count('T')
    Total_length = len(gene)
    #AT content is the percentage of A and T QUANTITY divided by the total length.
    AT_percentage = (A_count + T_count)/Total_length
    return AT_percentage

#This for loop cycles through each line in the provided all_lines variable. 
for line in all_lines:
    #The program needs to output single elements of the string, so I broke up the string
    #into a list that the program can grab individual elements of. 
    split_line = line.split(',')
    #If the AT_content definition for the second item of the split_line list, the gene sequence,
    # is less than 0.5 AND the 4th item of the split_line list, the expression level, is above 200,
    # then the gene name is printed.
    # An initial run of this program was yielding nothing but 0s as output.
    # It turns out that my conversion to int was rounding the AT content down to 0.
    # I used the below print output to diagnose that issue.
    # print((AT_content(split_line[1])))
    
    if int(AT_content(split_line[1])) < 0.5 and int(split_line[3]) > 200:
        print ("The gene name is " + (split_line[2]) )
    
