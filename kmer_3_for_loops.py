# This function generates all the possible combinations of 4 bases in sets of 3.
# The outer for loop defines the first base. The middle for loop defines the
# middle base and the innermost for loop defines the last base. 
def generate_trimers():
    bases = ['A', 'T', 'G', 'C']
    result = []
    for base1 in bases:
        for base2 in bases:
            for base3 in bases:
                result.append(base1 + base2 + base3)
    print(result)
generate_trimers()
