from itertools import product

def compute_reverse_complement(sequence):
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
    return reverse_complement

def generate_reverse_comp_hash(length):
    all_hash=generate_all_subseq(length)
    reverse_comp_hash={}
    for key in all_hash.keys():
        reverse_comp_hash[key]=compute_reverse_complement(key)
    return reverse_comp_hash

def generate_all_subseq(length):
    # Generate all possible sequences of length using 'ATCG'
    sequences = [''.join(seq) for seq in product('ATCG', repeat=length)]

    # Create a dictionary with each sequence as key and value initialized to 0
    sequence_dict = {seq: 0 for seq in sequences}

    return sequence_dict

def hamming_distance(sequence_p, sequence_q):
    hamming_d=0
    for ind, _ in enumerate(sequence_p):
        if sequence_p[ind]!=sequence_q[ind]:
            hamming_d+=1
    return hamming_d

def hash_sequence(sequence, k):
    '''
    Converts a sequence into
    k-mers by using a sliding window.
    '''
    hash = {}
    for pos in range(len(sequence) - k + 1):
        current_kmer = sequence[pos:pos + k]
        current_count = hash.get(current_kmer, 0)
        hash[current_kmer] = current_count + 1
    return hash

def find_kmers_in_window(window, k, target_t):
    counts=hash_sequence(window, k)
    target_kmers = [kmer for kmer, count in counts.items() if count >= target_t]
    return target_kmers

