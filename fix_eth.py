#!/usr/bin/env python

import sys

def process_text_file(input_file, output_file, target_string):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        skip_next_lines = False
        counter = 0

        for line in infile:
            # Check if the line contains the target string
            if target_string in line:
                skip_next_lines = True
                outfile.write(line)

            if skip_next_lines and counter < 6:
                counter += 1
            else:
                outfile.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: fix_eth <input_file> <output_file>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        target_string = "eth0:"  # Replace with the string you are searching for

        process_text_file(input_file_path, output_file_path, target_string)
