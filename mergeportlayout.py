import sys
import os

def merge_ports(infile1, infile2, outfile):
    with open(infile1, 'r') as inputfile1:
        file1lines = inputfile1.readlines()
    with open(infile2, 'r') as inputfile2:
        file2lines = inputfile2.readlines()
    with open(outfile, 'w') as outputfile:
        counter = 0
        for line in file1lines:
            templine = line.strip()
            outline = templine+"  --->  "+file2lines[counter]
            counter += 1
            outputfile.writelines(outline)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: mergeportlayout <original_input_yaml>")
    else:
        inputfilename = sys.argv[1]
        inputfilename_stripped, extension = os.path.splitext(inputfilename)
        outputfilename = inputfilename_stripped+'-merge.yaml'
        strippedfilename = inputfilename_stripped+'-strip.yaml'
        formattedfilename = inputfilename_stripped+'-formatted.yaml'
        print("inputfilename: ", inputfilename)
        print("inputfilename_stripped: ", inputfilename_stripped)
        print("outputfilename: ", outputfilename)
        print("strippedfilename: ", strippedfilename)
        print("formattedfilename: ", formattedfilename)
        merge_ports(strippedfilename, formattedfilename, outputfilename)

if __name__ == "__main__":
    main()