# This program is called "Double_digest.py" and it is part of the Regular Expression chapter
# from the book Biologists for Python. A file called dna.txt is provided in the chapter 7
# exercises folder. The program needs to predict the fragment lengths we'll get if we digest
# the sequence with two made-up enymes. AbcI has a recognition site of ANT/AAT. AbcII has a 
# recognition site of GCRW/TG. The forward slashes represent the cutting sites of the enzyme.
import re
# This opens the dna.txt file and then stores each of the lines in the variable dna_file_lines.
# It also removes any new line characters.
dna_file = open("dna.txt")
dna = dna_file.read().rstrip("\n")
# This prints the total length of the input DNA string.
print("The total length of the DNA string is: " + str(len(dna)))
# enzyme_cuts will be a list that stores all of the different fragments. It's initialized as 0
# in the text solutions, but I've just listed it as an empty list. As you'll see down the line,
# the presence of the total length of the dna covers the 0 fragment length. 0 fragment length
# and listing the total length of the string are equivalent situations. 
enzyme_cuts = []
# AbcI restriction enzyme fragment determination
# re.search doesn't work when more than one item is being searched for. re.finditer can be used
# to find multiple iterations of the search pattern. AbcI has a recognition site of ANT/AAT. N is 
# [ATGC] At first I was tempted to use a period in between the A and the T to cover the "N" being 
# there, but then I recalled that this is DNA, so ATGC is the only option; that's why those letters
# are held within brackets. The brackets indicate that any of those letters will appear once
# in the pattern. The dna variable from above is what's searched through. Then a for loop is
# is used to cycle through all of the pattern iterations that were found and stored in the match
# variable. The previously defined enzyme_cuts variable is appended the matching pattern. .start
# is used to go from the beginning (or the most recent cut) all the up to + 3 characters past the
# cut site. It's + 3 characters because there are three characters before the restriction enzyme 
# site. 
AbcI_matches = re.finditer(r"A[ATGC]TAAT", dna)
for match in AbcI_matches:
    enzyme_cuts.append(match.start() + 3)
# AbcII restriction enzyme fragment determination
# AbcII has a recognition site of GCRW/TG. R is A or G. W is A or T. This re.finditer operates
# in the same fashion as the AbcI matches. The difference is that the 2nd index positions needs
# to be A or G [AG] and the third position needs to be A or T [AT]. The brackets allow for only 
# one of the characters within the list. Either character is fine. The + 4 characters in the append
# statement is because the recognition site has 4 characters before the cut site. 
AbcII_matches = re.finditer(r"GC[AG][AT]TG", dna)
for match in AbcII_matches:
    enzyme_cuts.append(match.start() + 4 )
# The program has found the cut sites of the two enzymes, but has not listed the possibility of no
# cuts occurring. Using append for the total length of the initial dna string covers that possibility.
# The list of the cut sites is organized using 'sorted' and they're printed to the terminal. 
enzyme_cuts.append(len(dna))
organized_cuts = sorted(enzyme_cuts)
print("The different cut sizes are organized by length: ")
print(organized_cuts)
# This for loop goes through the whole range of the cut sizes (from 1 to the total length.)
# Note that it starts at 1 instead of 0. This allows for the 1th index position to start with the
# second component of the list and the 0th index position to have the 1st component of the list.
# i and i-1 are used to grab a 'current' position and a 'previous' position. Those are then subtracted
# from each other to get all of the available fragment lengths. 
for i in range(1, len(organized_cuts)):
    current_cut_location = organized_cuts[i]
    last_cut_location = organized_cuts[i-1]
    fragment_length = current_cut_location - last_cut_location
    print("Fragment " + str(i) + " is: " + str(fragment_length))
