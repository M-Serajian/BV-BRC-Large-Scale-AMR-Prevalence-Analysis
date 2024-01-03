#!/usr/bin/env python
import os
import csv
import argparse
import sys


# Define color variables
red_color = '\033[91m'  # ANSI escape code for red
green_color = '\033[92m'  # ANSI escape code for green
reset_color = '\033[0m'  # ANSI escape code to reset color

class FileNotFoundError(Exception):
    pass

class EmptyFileError(Exception):
    pass

class DirectoryNotFoundError(Exception):
    pass

def process_arguments():
    parser = argparse.ArgumentParser(description="Process FASTA files and save corrected CSV files.")
    parser.add_argument("-i", "--input", required=True, help="Input directory containing FASTA files.")
    parser.add_argument("-o", "--output", required=True, help="Output directory to save corrected CSV files.")

    args = parser.parse_args()

    # Check if the input file exists
    input_file = args.input
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{red_color}Error: File '{input_file}' not found.{reset_color}")

    # Check if the input file is empty
    if os.path.getsize(input_file) == 0:
        raise EmptyFileError(f"{red_color}Error: File '{input_file}' is empty.{reset_color}")

    # Check if the output directory exists
    output_dir = args.output
    if not os.path.exists(output_dir):
        raise DirectoryNotFoundError(f"{red_color}Error: Directory '{output_dir}' not found.{reset_color}")

    return args

def modify_text_file(input_path,output_path):
    with open(input_path, 'r') as file:
        content = file.read()

    last_letter_index = None
    for i, char in enumerate(reversed(content)):
        if char.isalpha():
            last_letter_index = len(content) - i - 1
            break

    if last_letter_index is not None:
        modified_content = content[:last_letter_index + 1]
        modified_content = modified_content.rstrip('\n') + '\n'
    else:
        modified_content = content + '\n'

    with open(output_path, 'w') as file:
        file.write(modified_content)
# Example usage


def main():
    try:
        args = process_arguments()
        
        # Extract the base name from the input file path
        file_name = os.path.basename(args.input)
        print(file_name)
        output_file_directory = os.path.join(args.output, file_name)

        print(output_file_directory)
        modify_text_file(args.input,output_file_directory)

    except (FileNotFoundError, EmptyFileError, DirectoryNotFoundError) as e:
        print(str(e))
        sys.exit(1)

      
if __name__ == "__main__":
    main()

