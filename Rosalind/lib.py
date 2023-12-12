from helpers import find_kmers_in_window, hash_sequence, hamming_distance
import numpy as np

def BA1H(input_list):
    '''
    Approximate occurences of patterns in a string'
    '''
    match_string=input_list[0]
    sequence=input_list[1]
    d_threshold=int(input_list[2])
    k=len(match_string)
    positions=[]
    for ind in range(0,len(sequence)-k+1):
        seq_kmer=sequence[ind:ind+k]
        hamming_d=hamming_distance(seq_kmer, match_string)
        if hamming_d<=d_threshold:
            positions.append(ind)
    positions=[str(x) for x in positions]
    print(' '.join(positions))
    return ' '.join(positions)


def BA1G(input_list):
    '''
    Find Hamming distance between two sequences.

    Complexity: O(len(sequences))
    '''
    sequence_p=input_list[0]
    sequence_q=input_list[1]
    hamming_d=hamming_distance(sequence_p, sequence_q)
    print(hamming_d)
    return hamming_d


def BA1F(input_list):
    '''
    Find minimal skew between count
    of G and C from sequential prefixes.
    Complexity: O(len(sequence))
    '''
    CG_counts={'G':0,
               'C':0}
    sequence=input_list[0]
    skews=[0]
    for i in range(0, len(sequence)):
        if sequence[i]=='C':
            CG_counts['C']+=1
        if sequence[i]=='G':
            CG_counts['G']+=1
        skew=CG_counts['G']-CG_counts['C']
        skews.append(skew)
    minimums=np.where(skews == np.array(skews).min())[0].tolist()
    str_minimums=[str(x) for x in minimums]
    print(' '.join(str_minimums))
    return ' '.join(str_minimums)
    

def BA1E(input_list):
    '''
    Find patterns of forming clumps in string.
    k--> kmer length
    L--> length of clump (window)
    t--> how many times the kmer occurs
    in clump

    Complexity: O(len(sequence)*L)
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
    solution_list=set(solution_list)
    solution_list=list(solution_list)
    print(' '.join(solution_list))
    return ' '.join(solution_list)



def BA1D(input_list):
    '''
    Finds the locations of a
    substring in a string.
    Complexity: O(len(sequence)*k)
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
    Complexity: O(len(sequence))
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
    '''
    Count number of times kmer occurs in genome.
    '''
    sequence=input_list[0]
    kmer=input_list[1]
    k=len(kmer)
    count=0
    for ind in range(0,len(sequence)-k+1):
        if sequence[ind:ind+k]==kmer:
            count+=1
    print(count)
    return count

    


