#!/usr/bin/env python
import os
import csv
import argparse
import sys
saving_DIR="/home/m.serajian/share/MTB_Database/DV-BRC_corrected/"
input_DIR="/home/m.serajian/share/MTB_Database/DV-BRC-Sientific-reports-Jan2024/"

file_name= sys.argv[1]

print("input:")
saving_DIR=saving_DIR+file_name
print(saving_DIR)
print("output:")
input_DIR=input_DIR+file_name
print(input_DIR)

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

modify_text_file(input_DIR,saving_DIR)