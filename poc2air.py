import sys
import os
import argparse

is_mapped = False
is_embedded = False

parser = argparse.ArgumentParser(description='Convert physical (POC) to virtual (AIR) Cumulus YAML configuration file')
parser.add_argument('poc_file', help='provide the saved YAML configuration file from the physical switch')
parser.add_argument('-m', '--mapped', action='store_true', help='displays mapped interfaces from POC to AIR')
parser.add_argument('-e', '--embed', action='store_true', help='will embed # comments in AIR file with source interface')
args = parser.parse_args()

if args.poc_file:
    poc_file = args.poc_file
    
if args.mapped:
    is_mapped = args.mapped
    
if args.embed:
    is_embedded = args.embed

def find_switch_ports(input_file, output_file):
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    filtered_lines = [line for line in lines if "swp" in line and ":" in line and "type: swp" not in line]

    with open(output_file, 'w') as output_file:
        output_file.writelines(filtered_lines)

def define_new_ports(input_file, output_file):
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    with open(output_file, 'w') as output_file:
        counter = 1
        for line in lines:
            newline = "swp" + str(counter) + ":"
            output_file.writelines(newline+"\n")
            counter += 1

def replace_switch_ports(input_file, orig_file, output_file):
    with open(input_file, 'r') as input_file:
        lines = input_file.readlines()

    with open(orig_file, 'r') as orig_file:
        origlines = orig_file.readlines()

    counter = 0
    with open(output_file, 'w') as output_file:
        for line in origlines:
            if "swp" in line and ":" in line and "type: swp" not in line:
                if is_embedded:
                    newline = "\n# " + line.strip() + "\n    " + lines[counter]
                else:
                    newline = "\n    " + lines[counter]
                counter += 1
            else:
                newline = line
            output_file.writelines(newline)

def merge_ports(infile1, infile2, outfile):
    with open(infile1, 'r') as inputfile1:
        file1lines = inputfile1.readlines()
    with open(infile2, 'r') as inputfile2:
        file2lines = inputfile2.readlines()
    with open(outfile, 'w') as outputfile:
        counter = 0
        for line in file1lines:
            templine = line.strip()
            if len(templine) < 8:
                templine += "\t"
            outline = templine+"\t--->\t\t"+file2lines[counter]
            counter += 1
            outputfile.writelines(outline)

def main():
    inputfilename = poc_file
    inputfilename_stripped, extension = os.path.splitext(inputfilename)
    outputfilename = inputfilename_stripped+'_air.yaml'
    mappedfilename = inputfilename_stripped+'_mapped.yaml'
    strippedfilename = inputfilename_stripped+'_strip.yaml'
    formattedfilename = inputfilename_stripped+'_formatted.yaml'
    
    print("poc2air.")
    print(f"input file:   {inputfilename}")
    print(f"stripped:     {inputfilename_stripped}")
    if is_mapped:
        print(f"mapped:       {mappedfilename}")
    print(f"output file:  {outputfilename}")

    find_switch_ports(inputfilename, strippedfilename)
    define_new_ports(strippedfilename, formattedfilename)
    replace_switch_ports(formattedfilename, inputfilename, outputfilename)
    merge_ports(strippedfilename, formattedfilename, mappedfilename)
    print("done.\n")

if __name__ == "__main__":
    main()

