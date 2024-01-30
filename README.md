Convert all interfaces from original cumulus YAML config output into swpXX interfaces YAML file for use with AIR.

Usage: python3 poc2air2.py <input_yaml_file> <map_file>

Map file:
The map_file will be a text file describing the relation between the physical interface on the switch and the AIR/NVUE interface.
The format is <interface_name>::<air_interface_name>

Example:
$ cat mytest.dot
swp14::swp1
swp15::swp2
swp44s0::swp31
swp44s1::swp32

*NOTE* <air_interface_name> should match the interfaces used in the bringup of the AIR simulation.

To test:

git clone https://github.com/Cloudofyou/poc2air

cd poc2air

python3 poc2air2.py <switch.yaml> <switch-map.dot>
