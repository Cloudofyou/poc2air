import sys

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
               newline = "    " + lines[counter]
               counter += 1
            else:
               newline = line
            output_file.writelines(newline)

def main():
    if len(sys.argv) != 3:
        print(f"Usage: poc2air <input_yaml> <output_yaml>")
    else:
        inputfilename = sys.argv[1]
        outputfilename = sys.argv[2]
        find_switch_ports(inputfilename, 'output.txt')
        define_new_ports('output.txt', 'formatted.txt')
        replace_switch_ports('formatted.txt', inputfilename, outputfilename)

if __name__ == "__main__":
    main()