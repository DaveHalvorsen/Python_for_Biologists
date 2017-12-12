# This program creates 9 folders. Folder 1 is for DNA sequences that are 100 - 199 bases long, 
# folder 2 is for 200 - 299 ... folder 9 is 900 - 999 bases long. The initial files are not to
# be deleted. They are copied over into the new folders. This program iterates over the files 
# in a folder, iterates over the lines of each of those files, figures out which bind each DNA
# sequence needs to go to and then write the DNA sequence to that new folder. 

# os is imported because it's required for making the folders.
import os

# This code creates a "New_Directory". Make sure to use forward slashes (/) instead of back slashes (\)
# It is important to note if those files are already present ... if they're around, this will post an error
# message. It would be better to use os.path.exists to check if the folder is present in the for loop if
# I work on this program again in the future. 
for i in range (1, 10):
    os.mkdir("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_" + str(i))

# save_number is used as the file name with a postfix of ".txt" It gets incremented with each run of the
# outer for loop.
save_number = 1

# This for cycles through all of the files in the directory listed below and the print statement notifies
# the user of whatever file name is currently being accessed. 
for file_name in os.listdir("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Files"):
    print("Reading data from file: " + file_name)
    # This opens the current file_name for reading each individual line. The inner for loop removes the 
    # new line characters and then it measures the length of the dna sequence for the current line. 
    # The length of the current line is printed to the terminal. 
    dna_file = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Files/" + file_name)
    for line in dna_file:
        dna = line.rstrip("\n")
        dna_length = len(dna)
        print("\tFound a length of: " + str(dna_length))
    # This if/elif/else loop has different reactions based on the length of the dna sequence (as measured
    # in the previous for loop). Current file lines are added to the file located in that directory. The new
    # lines are appended to the previously added lines. Each folder direction is changed based on the save_number.
    # The save_number gets incremented by 1 after each run of the cycle.
    if 100 <= dna_length <= 199:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_1/" + str(save_number) + ".txt", "w")
        save.write(dna)
        save.close()
    elif 200 <= dna_length <= 299:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_2/" + str(save_number) + ".txt", "w")
        save.write(dna)
        save.close()
    elif 300 <= dna_length <= 399:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_3/" + str(save_number) +".txt", "w")
        save.write(dna)
        save.close()
    elif 400 <= dna_length <= 499:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_4/" + str(save_number) +".txt", "w")
        save.write(dna)
        save.close()
    elif 500 <= dna_length <= 599:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_5/" + str(save_number)+".txt", "w")
        save.write(dna)
        save.close()
    elif 600 <= dna_length <= 699:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_6/" + str(save_number)+".txt", "w")
        save.write(dna)
        save.close()
    elif 700 <= dna_length <= 799:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_7/" + str(save_number) +".txt", "w")
        save.write(dna)
        save.close()
    elif 800 <= dna_length <= 899:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_8/" + str(save_number) +".txt", "w")
        save.write(dna)
        save.close()
    elif 900 <= dna_length <= 999:
        save = open("D:/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Folder_9/" + str(save_number) +".txt", "w")
        save.write(dna)
        save.close()    
    # This else shouldn't be required, but I've kept it here just in case one of the files doesn't fit in the above structure.
    # A message will be printed about the error if that happens. 
    else:
        print("This file name does not fit within the logic structure: " + file_name)
    save_number += 1
