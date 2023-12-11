from lib import BA1B, BA1B_data_parsing

caller_dict = {
    'BA1B': {
        'description': 'find_most_frequent_kmer',
        'algorithm_function': BA1B,
        'data_parsing_function': BA1B_data_parsing,
        'debug_dataset': 'rosalind_ba1b.txt'
        
    }
}