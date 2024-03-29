from lib import BA1M,BA1L, BA1K, BA1J, BA1I, BA1H, BA1G, BA1F, BA1E, BA1D, BA1C, BA1B, BA1A

caller_dict = {

    'BA1M': {
        'description': 'Number to genetic sequence',
        'algorithm_function': BA1M,
        'dataset': 'rosalind_ba1m.txt'
    },

    'BA1L': {
        'description': 'Genetic sequence to number',
        'algorithm_function': BA1L,
        'dataset': 'rosalind_ba1l.txt'
    },

    'BA1K': {
        'description': '''
            Number of times k-mer
            appears in sequence
            with k-mers appear in
            lexicographic order.
            ''',
        'algorithm_function': BA1K,
        'dataset': 'rosalind_ba1k.txt'
    },

    'BA1J': {
        'description': '''Frequent words with mismatches
            and reverse complements. Find
            pattern that maximizes the sum
            of its counts with mismatches 
            and its reverse complement counts 
            with mismatches.''',
        'algorithm_function': BA1J,
        'dataset': 'rosalind_ba1j.txt'
    },


    'BA1I': {
        'description': 'Find all most frequent kmers up to d mismatches in text.',
        'algorithm_function': BA1I,
        'dataset': 'rosalind_ba1i.txt'
    },

    'BA1H': {
        'description': 'Approximate occurences of patterns in a string',
        'algorithm_function': BA1H,
        'dataset': 'rosalind_ba1h.txt'
    },

    'BA1G': {
        'description': 'Find Hamming distance between two sequences.',
        'algorithm_function': BA1G,
        'dataset': 'rosalind_ba1g.txt'
    },

    'BA1F': {
        'description': 'Find minimal skew between count of G and C from sequential prefixes.',
        'algorithm_function': BA1F,
        'dataset': 'rosalind_ba1f.txt'
    },

    'BA1E': {
        'description': 'Find patterns of forming clumps in string',
        'algorithm_function': BA1E,
        'dataset': 'rosalind_ba1e.txt'
    },

    'BA1D': {
        'description': 'Return locations of substring in string',
        'algorithm_function': BA1D,
        'dataset': 'rosalind_ba1d.txt'
    },

    'BA1C': {
        'description': 'Find reverse complement of string',
        'algorithm_function': BA1C,
        'dataset': 'rosalind_ba1c.txt'
    },

    'BA1B': {
        'description': 'find most frequent kmer',
        'algorithm_function': BA1B,
        'dataset': 'rosalind_ba1b.txt'
        
    },

    'BA1A': {
        'description': 'Compute nr of times kmer appears in string',
        'algorithm_function':BA1A,
        'dataset': 'rosalind_ba1a.txt'
    }

}