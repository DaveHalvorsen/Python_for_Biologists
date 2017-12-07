# This program is called High_low_medium.py. It is part of the Conditional tests
# chapter from the book Python for Biologists. This program accesses the file called
# data.csv and prints out the gene name and stating whether the AT_content is 
# high (> 0.65), low (<0.45) or medium (0.45 <= AT_content <= 0.65). It's
# very important to carefully cover the whole range of numbers. The greater than
# or equal sign and less than equal sign is important because otherwise 0.45 and
# 0.65 cases would not be included in the base conditions at all. #

# First the data.csv file is opened and stored in a variable called all_lines that
# can be used to cycle through with a for loop.
data_file = open("data.csv")
all_lines = data_file.readlines()

# This AT_content was one of the original exercises. It has been turned in to a definition to
# be called upon within the upcoming for loop.
def AT_content(gene):
    A_count = gene.upper().count('A')
    T_count = gene.upper().count('T')
    Total_length = len(gene)
    #AT content is the percentage of A and T QUANTITY divided by the total length.
    AT_percentage = (A_count + T_count)/Total_length
    return AT_percentage

# This for loop cycles through each line in the provided all_lines variable. 
for line in all_lines:
    # The program needs to output single elements of the string, so I broke up the string
    # into a list that the program can grab individual elements of. 
    split_line = line.split(',')
    
    # This if elif else structure splits up the output into 4 possibilities. It calls the AT content definition from
    # earlier and then checks for < 0.45; >= 0.45 <=0.65; and >0.65. The gene sequence is printed, along with it's AT
    # content and whether it's AT content is low, medium, or high. There's a 4th option of the AT content not being
    # within the range of possibilities ... I only added that to check for the possibility that my conditionals didn't
    # account for every kind of AT content output. #
    if AT_content(split_line[1]) < 0.45:
        print("The gene " + str(split_line[2]) + " has an AT content value of " + str(AT_content(split_line[1])) + " LOW.")
        print("It's sequence is: " + split_line[1] + "\n")
    elif AT_content(split_line[1]) >= 0.45 and AT_content(split_line[1]) <= 0.65:
        print("It's sequence is: " + split_line[1] + "\n")
        print("The gene " + str(split_line[2]) + " has an AT content value of " + str(AT_content(split_line[1])) + " MEDIUM.")
    elif AT_content(split_line[1]) > 0.65:
        print("The gene " + str(split_line[2]) + " has an AT content value of " + str(AT_content(split_line[1])) + " HIGH.") 
        print("It's sequence is: " + split_line[1] + "\n")
    else: 
        print("The gene's expression value has not been programmed for.")


    
    
