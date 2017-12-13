# This program counts kmers for all of the *.dna files in the DNA_files folder in my computer. 
# The full path to get there is: C:/Users/David/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Files
# The program could be changed to do this to any directory by altering the os.listdir location.
# kmers are used as part of the process to identify full genomes with DNA sequencing. It's not
# possible to read the entirety of the genome in one go, so individiaul reads are broken up into
# small pieces and then the overlapping pieces are used to find contiguous sections of DNA. This
# program allows the user to specify the length of the kmers, 1st argument, and the cutoff point
# for #s of replicate kmers found, 2nd argument. Those specifications are done in the command line
# right after the "python Kmer_counting.py" code in the command line. 

# os is a module for manipulating files. sys is a module that allows for the usage of command 
# line options.
import os
import sys

# This program started out with allowing the user to input the kmer length and cutoff number
# after being prompted by the program. That code is now commented out because those options 
# are now handled in the command line when calling the program. I preferred this old way
# because it's more intuitive for the user to work with, but the excercise calls for using sys. 
# kmer_size = int(input("What is the kmer length? "))
# count_cutoff = int(input("What is the cutoff number? "))

# Command line arguments are strings that you type on the command line after the name of the
# program that you want to run. sys.argv is referred to as the special list. The first element
# of sys.argv is the program itself. That's why the arguments start at 1 here. kmer_size is the
# length of the generated DNA fragments and count_cutoff is the minimum number of replicates
# required to trigger the final print at the end of the program. 
kmer_size = int(sys.argv[1])
count_cutoff = int(sys.argv[2])

# This function accepts dna & kmer_size and starts out an empty list for kmers to be added to.
def split_dna(dna, kmer_size):
    kmers = []
    # This cycles through the provided dna sequence and stops at the last remaining start 
    # point of a kmer. Note that the end of the for loop is the length of the dna sequence
    # - the kmer_size + 1. The length starts at 1 and the index starts at 0, so + 1 is necessary
    # to equilibrate them. It wouldn't be necessary if list slicing ends were inclusive, but 
    # they aren't. This for loop can only handle one line of dna at a time. It gets called 
    # by the for loop below.
    for start in range(0, len(dna) - kmer_size + 1, 1):
        kmer = dna[start:start+kmer_size]
        kmers.append(kmer)
    return kmers

# This empty dictionary will be used to store all of the kmers and their counts.
kmer_counts = {}

# This for loop iterates over every file within the directory. The if beneath it ensures that
# only files with the .dna ending are run in the program cause we don't want this python code
# to be run (if it was in the same directory). Each file that is opened is printed to the screen. 
for file_name in os.listdir("C:/Users/David/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Files"):
    if file_name.endswith(".dna"):
        print("Reading data from file: " + file_name)
    # This opens the current file_name for reading each individual line. The inner for loop removes the 
    # new line characters and then it measures the length of the dna sequence for the current line. 
    # The length of the current line is printed to the terminal. 
        dna_file = open("C:/Users/David/Dropbox/Python_for_Biologists/My_Code/File_System/DNA_Files/" + file_name)
        # for each line in the dna file the new lines are removed and saves as the dna variable.
        for line in dna_file:
            dna = line.rstrip("\n")
            # The split_dna function is called AS THE GROUP to run individual kmers from ... that's
            # brilliant and very much not my idea; it's from the solutions key. The current_count
            # is defaulted to 0 (with the .get method) OR it's updated value is stored there. This
            # loop is only run when a kmer hit is detected, so the current_count is +1 and then the
            # kmer_counts dictionary, with a kmer key, is given the new_count for that kmer.
            for kmer in split_dna(dna, kmer_size):
                current_count = kmer_counts.get(kmer, 0)
                new_count = current_count + 1
                kmer_counts[kmer] = new_count
# This prints out the kmer_counts dictionary. 
print(kmer_counts)

# kmer & acount are the variables that are given values from the .items call on the kmer_counts 
# dictionary. If the kmer keys count is higher than the count_cutoff, the minimum # that the
# user specified, than the kmer key and the count is printed to the terminal.  
for kmer, count in kmer_counts.items():
    if count > count_cutoff:
        print(kmer + " : " + str(count))


