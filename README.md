Convert all interfaces from original cumulus YAML config output into swpXX interfaces YAML file for use with AIR.

Usage: python3 poc2air.py <input_yaml_file>

*TEMP* Will clean-up after final solution but this script creates multiple files based on basename of input yaml file:
IFN = input_yaml_file_name_without_yaml_extension (example: mytest.yaml, IFN == mytest)
IFN-strip.yaml        :  List of interfaces in order from original yaml file
IFN-formatted.yaml    :  List of interfaces sequentially to match length of IFN-strip.yaml
IFN-AIR.yaml          :  Final YAML config output with interfaces remapped to sequential swpXX interface names

If you use the additional script: python3 mergeportlayout.py <input_yaml_file>, it will produce:

IFN-merge.yaml        :  List of original yaml interfaces and what they are mapped to in the final AIR yaml file

To test:
git clone https://github.com/Cloudofyou/poc2air.git
cd poc2air
python3 poc2air.py sample-leaf.yaml
python3 mergeportlayout.py sample-leaf.yaml

