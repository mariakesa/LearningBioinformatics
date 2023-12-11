from lib import BA1B
from data_dict import caller_dict
from pathlib import Path
import argparse

def runner(debug, ex_data):
    current_dir = Path(__file__)
    
    if debug:
        print('In debug mode!')
        debug_path = current_dir / Path('data') / Path('debug') / caller_dict[debug]['debug_dataset']
        function = caller_dict[debug]['function']
        print(function.__name__)
        # Rest of your code for debug mode
    elif ex_data:
        print('In exercise mode!')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your script description")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--debug', type=str, help='Debug mode with a custom value')
    group.add_argument('--ex_data', type=str, help='Exercise mode with a custom value')
    
    args = parser.parse_args()
    
    runner(debug=args.debug, ex_data=args.ex_data)
