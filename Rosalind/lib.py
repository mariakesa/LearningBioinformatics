from helpers import find_kmers_in_window, hash_sequence
import numpy as np

def BA1E(input_list):
    '''
    Find patterns of forming clumps in string.
    k--> kmer length
    L--> length of clump (window)
    t--> how many times the kmer occurs
    in clump
    '''
    sequence=input_list[0]
    k, L, t = input_list[1].split(' ')
    k=int(k)
    L=int(L)
    t=int(t)
    solution_list=[]
    for ind in range(0,len(sequence)-L+1):
        window = sequence[ind:ind+L]
        found_kmers = find_kmers_in_window(window,k, t)
        if found_kmers:
            solution_list+=found_kmers
    solution_list=np.unique(solution_list)
    solution_list=list(solution_list)
    print(' '.join(solution_list))
    return ' '.join(solution_list)



def BA1D(input_list):
    '''
    Finds the locations of a
    substring in a string.
    '''
    kmer=input_list[0]
    sequence=input_list[1]
    k=len(kmer)
    locations=[]
    for ind in range(0,len(sequence)-k+1):
        if sequence[ind:ind+k]==kmer:
            locations.append(str(ind))
    print(' '.join(locations))
    return ' '.join(locations)


def BA1C(input_list):
    '''
    Find reverse complement of sequence.
    '''
    sequence=input_list[0]
    reverse_dct ={
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    reverse_complement=''
    for s in range(-1,-len(sequence)-1, -1):
        rev=reverse_dct[sequence[s]]
        reverse_complement+=rev
    print(reverse_complement)
    #print(len(sequence), len(reverse_complement))
    return reverse_complement

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

def BA1A(input_list):
    sequence=input_list[0]
    kmer=input_list[1]
    k=len(kmer)
    count=0
    for ind in range(0,len(sequence)-k+1):
        if sequence[ind:ind+k]==kmer:
            count+=1
    print(count)
    return count

    


