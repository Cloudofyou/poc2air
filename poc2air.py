import sys
import os

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
                newline = "# " + line + "    " + lines[counter]
#               newline = "    " + lines[counter]
                counter += 1
            else:
                newline = line
            output_file.writelines(newline)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: poc2air <input_yaml>")
    else:
        inputfilename = sys.argv[1]
        inputfilename_stripped, extension = os.path.splitext(inputfilename)
        outputfilename = inputfilename_stripped+'-AIR.yaml'
        strippedfilename = inputfilename_stripped+'-strip.yaml'
        formattedfilename = inputfilename_stripped+'-formatted.yaml'
        print("inputfilename: ", inputfilename)
        print("inputfilename_stripped: ", inputfilename_stripped)
        print("extension: ", extension)
        print("outputfilename: ", outputfilename)
        print("strippedfilename: ", strippedfilename)
        print("formattedfilename: ", formattedfilename)
        find_switch_ports(inputfilename, strippedfilename)
        define_new_ports(strippedfilename, formattedfilename)
        replace_switch_ports(formattedfilename, inputfilename, outputfilename)

if __name__ == "__main__":
    main()
