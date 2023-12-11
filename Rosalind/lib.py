from helpers import hash_sequence

def BA1B(input_list):
    '''
    Most frequent kmer

    Algorithm is linear in sequence length.
    '''
    print(input_list)
    sequence=input_list[0]
    k=int(input_list[1])
    hash_table=hash_sequence(sequence,k)

    max_count = 0
    most_frequent_kmers = []

    for kmer, count in hash_table.items():
        if count > max_count:
            max_count = count
            most_frequent_kmers = [kmer]
        elif count == max_count:
            most_frequent_kmers.append(kmer)

    print(' '.join(most_frequent_kmers))

    return most_frequent_kmers, max_count

    


