
# Nested for loops WITHOUT the ability to change length generation of kmer combinations
def generate_kmers_nested():
    bases = ['A', 'T', 'G', 'C']
    result = []
    for base1 in bases:
        for base2 in bases:
            for base3 in bases:
                result.append(base1 + base2 + base3)
    return result
# Nested for loops WITH the ability to change the length of generated kmer combinations
def generate_kmers_iterative(user_choice_length):
    result = ['']
    for i in range(user_choice_length):
        new_result = []
        for kmer in result:
            for base in ['A', 'T', 'G', 'C']:
                new_result.append(kmer + base)
        result = new_result
    return result
# Recursive generation of kmer combinations
def generate_kmers_recursive(user_choice_length):
    if user_choice_length == 1:
        return ['A', 'T', 'G', 'C']
    else:
        result = []
        for sequence in generate_kmers_recursive(user_choice_length - 1):
            for base in ['A', 'T', 'G', 'C']:
                result.append(sequence + base)
        return result

# print(generate_kmers_recursive(5))
while True:
    print("Choose the type of kmer combination generation that you want.")
    user_choice_method = (input("For nested loops enter 'NESTED' For recursive generation enter 'RECURSIVE' For iterative nested loops enter 'ITERATIVE' to quit enter 'QUIT' \n")).upper()
    user_choice_length = int(input("How long do you want the kmer combinations to be? \n"))
    if user_choice_method == 'NESTED':
        print('Nested generation of kmers does not allow differences in length. The default is 3. Try another method.')
        print(generate_kmers_nested())
    elif user_choice_method == 'RECURSIVE':
        print('Recursively generating kmers ...')
        print(generate_kmers_recursive(user_choice_length))
    elif user_choice_method == 'ITERATIVE':
        print('Iteratively generating kmers ...')
        print(generate_kmers_iterative(user_choice_length))
    elif user_choice_method == 'QUIT':
        print('Exiting program ...')
        break
    else:
        print('I did not understand your input. ') 

