#!/usr/bin/env python

import sys
import os
import argparse

parser = argparse.ArgumentParser(description='Convert physical (POC) to virtual (AIR) Cumulus YAML configuration file')
parser.add_argument('poc_file', help='provide the saved YAML configuration file from the physical switch')
parser.add_argument('map_file', help='file which maps physical port to AIR port')

args = parser.parse_args()

if args.poc_file:
    poc_file = args.poc_file

if args.map_file:
    map_file = args.map_file

def remap_switch_ports_to_air_ports(map_file, input_file, output_file):
    pairs_list = []
    with open(map_file, 'r') as inputfile:
        for line in inputfile:
            parts = line.strip().split("::")
            if len(parts) == 2:
                pairs_list.append((parts[0],parts[1]))

    with open(input_file, 'r') as inputfile:
        filelines = inputfile.readlines()

    with open(output_file, 'w') as outputfile:
        portflagged = False
        counter = 0
        for line in filelines:
            newline = line
            isfound = False
            for loop in range(len(pairs_list)):
                pair = pairs_list[loop]
                if pair[0] in line:
                    newline = line.replace(pair[0],pair[1])
                    isfound = True
            if isfound:
                outputfile.writelines(newline)
            else:
                if portflagged:
                    if "type: swp" in line:
                        portflagged = False
                else:
                    if "swp" in line and ":" in line and not "type:" in line:
                        portflagged = True
                    else:
                        if "model: " in newline:
                            newline = "    model: VX\n"
                        outputfile.writelines(newline)

def main():
    inputfilename = poc_file
    mapfilename = map_file
    inputfilename_stripped, extension = os.path.splitext(inputfilename)
    outputfilename = inputfilename_stripped+'-air.yaml'

    if not os.path.isfile(inputfilename):
        print(f"Error opening input YAML file: {inputfilename}")
        exit(1)

    if not os.path.isfile(mapfilename):
        print(f"Error opening input map file: {mapfilename}")
        exit(2)

    print("poc2air.")
    print(f"map file:     {mapfilename}")
    print(f"input file:   {inputfilename}")
    print(f"output file:  {outputfilename}")

    remap_switch_ports_to_air_ports(mapfilename, inputfilename, outputfilename)

if __name__ == "__main__":
    main()
