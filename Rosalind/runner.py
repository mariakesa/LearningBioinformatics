from data_dict import caller_dict
from pathlib import Path
import argparse

def open_data(data_path):
    try:
        with open(data_path, 'r') as file:
            # Read all lines from the file and store them in a list
            file_rows = file.readlines()

        file_rows=[x.strip() for x in file_rows]

        return file_rows

    except FileNotFoundError:
        print(f"The file '{data_path}' was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

def runner(debug, ex_data):
    current_dir = Path(__file__).parent
    
    if debug:
        print('In debug mode!')
        debug_path = current_dir / Path('data') / Path('debug') / caller_dict[debug]['debug_dataset']
        algorithm = caller_dict[debug]['algorithm_function']
        data = open_data(debug_path)
        algorithm(data)
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
