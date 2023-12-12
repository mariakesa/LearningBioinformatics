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

