def iteratively_generate_kmers(user_selected_length):
    final_result = ['']
    for i in range(user_selected_length):
        current_iteration_result = []
        for kmer in final_result:
            for base in ['A', 'T', 'G', 'C']:
                current_iteration_result.append(kmer + base)
        final_result = current_iteration_result
    return final_result
user_selected_length = int(input("How long do you want the kmer combinations to be? (Enter a digit, not a word.) "))
print(iteratively_generate_kmers(user_selected_length))
