#This exercise is from Chapter 4: Lists and Loops of the Python for Biologists book.
#This program is called Processing_DNA_in_a_file.py. It takes an input.txt file
#and: trims a sequencing adapter, writes the cleaned sequences to a new file, and
#prints the lengh of each sequence to the screen.
#These two lines open the input.txt file and save it as an iterable list.
my_file_name = open("input.txt")
all_lines = my_file_name.readlines()

#This is the destination file for the trimmed sequences.
new_file = open("trimmed_sequences.txt", "w")

#This for loop uses list slicing to remove the first 14 characters from each new line.
#The lengths of the trimmed and initial line sequences are determined.
#The trimmed sequences are stored in the new_file with a new line after each entry.
#The initial, trimmed and the difference between each length is displayed with a print. 
for line in all_lines:
    copy_this = line[14:]
    initial_line_length = len(line)
    line_length = len(copy_this)
    new_file.write(copy_this + "\n")
    print("The length of the sequence was initially: " + str(initial_line_length) + ". After cutting it's: " + str(line_length) + ". That's a difference of: " + str(initial_line_length - line_length)+ ".")

#These two lines close both of the files that were opened throughout the program. 
new_file.close()
my_file_name.close()
