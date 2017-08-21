#The book Python for Biologists claims to teach scientists programming.
#This is my solution to the Chapter 2 exercise: Complementing DNA.
#Complementary DNA is the binding partner for a given DNA strand, like this: A<->T & G<->C
#In this case, I calculate complement for the submitted string "my_dna."

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#Here, I use the replace method to make these letter changes: A<->T & G<->C
#Note that I don't simply replace A with T and then replace T with A.
#Try it yourself and you'll realize that the transition should only happen once.
#BUT, if you just make fully capitalized changes, like replacing A with T, you change things more than once.
#There are a few ways to handle this issue. I have chosen to convert to lowercase after complementing.
dna_complement = my_dna.replace("A", "t")
dna_complement = dna_complement.replace("T", "a")
dna_complement = dna_complement.replace("C", "g")
dna_complement = dna_complement.replace("G", "c")

#Now that the complement has been made with all lowercase letters, we can convert back.
#I call the upper method to create the upper case string that biologists are accustomed to.
dna_complement = dna_complement.upper()

#Now, I can print the new string dna_complement with an introductory string!
print("The DNA complement is: " + dna_complement)
