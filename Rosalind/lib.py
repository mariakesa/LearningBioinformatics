from helpers import generate_reverse_comp_hash, generate_all_subseq, find_kmers_in_window, hash_sequence, hamming_distance
import numpy as np

def BA1M(input_list):
    '''
    Number to genetic sequence.
    '''
    index=int(input_list[0])
    k=int(input_list[1])
    bases = ['A', 'C', 'G', 'T']
    pattern = ''
    for i in range(k):
        pattern += bases[index % 4]
        index = index // 4
    return pattern[::-1]

def BA1L(input_list):
    '''
    Genetic sequence to number
    '''
    seq = input_list[0]
    print(seq)
    encoding = {'A':0, 'C':1, 'G':2, 'T':3}
    k = len(seq)
    num = 0
    for i in range(k):
        print(encoding[seq[i]],k-i-1,pow(4, k-i-1))
        num += encoding[seq[i]] * pow(4, k-i-1)
    print(num)

def BA1K(input_list):
    '''
    Number of times k-mer
    appears in sequence
    with k-mers appear in
    lexicographic order.
    '''
    sequence=input_list[0]
    k=int(input_list[1])
    hash=generate_all_subseq(k)
    for s in range(0, len(sequence)-k+1):
        hash[sequence[s:s+k]]+=1
    sorted_dict = dict(sorted(hash.items()))
    print(' '.join(map(str, sorted_dict)))


def BA1J(input_list):
    '''
    Frequent words with mismatches
    and reverse complements. Find
    pattern that maximizes the sum
    of its counts with mismatches 
    and its reverse complement counts
    with mismatches. 
    '''
    sequence=input_list[0]
    k, d = input_list[1].split(' ')
    k=int(k)
    d=int(d)
    hash_table=generate_all_subseq(k)
    rev_hash=generate_reverse_comp_hash(k)
    for ind in range(0,len(sequence)-k+1):
        seq=sequence[ind:ind+k]
        for key in hash_table.keys():
            if hamming_distance(seq,key)<=d:
                hash_table[key]+=1
                hash_table[rev_hash[key]]+=1

    max_count = 0
    most_frequent_kmers = []

    for kmer, count in hash_table.items():
        if count > max_count:
            max_count = count
            most_frequent_kmers = [kmer]
        elif count == max_count:
            most_frequent_kmers.append(kmer)

    print(' '.join(most_frequent_kmers))

def BA1I(input_list):
    '''
    Find all most frequent kmers up to d mismatches in text.
    '''
    sequence=input_list[0]
    k, d = input_list[1].split(' ')
    k=int(k)
    d=int(d)
    hash_table=generate_all_subseq(k)
    for ind in range(0,len(sequence)-k+1):
        seq=sequence[ind:ind+k]
        for key in hash_table.keys():
            if hamming_distance(seq,key)<=d:
                hash_table[key]+=1

    max_count = 0
    most_frequent_kmers = []

    for kmer, count in hash_table.items():
        if count > max_count:
            max_count = count
            most_frequent_kmers = [kmer]
        elif count == max_count:
            most_frequent_kmers.append(kmer)

    print(' '.join(most_frequent_kmers))

def BA1H(input_list):
    '''
    Approximate occurences of patterns in a string.
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


def BA1G(input_list):
    '''
    Find Hamming distance between two sequences.

    Complexity: O(len(sequences))
    '''
    sequence_p=input_list[0]
    sequence_q=input_list[1]
    hamming_d=hamming_distance(sequence_p, sequence_q)
    print(hamming_d)


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
    


