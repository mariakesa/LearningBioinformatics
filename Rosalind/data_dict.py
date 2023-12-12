from lib import BA1E, BA1D, BA1C, BA1B, BA1A

caller_dict = {

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