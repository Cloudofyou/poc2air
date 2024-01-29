#!/usr/bin/env python

import yaml

def replace_breakout_with_state(yaml_content):
    for line in yaml_content.split('\n'):
        if 'breakout:' in line:
            yaml_content = yaml_content.replace(line, line.replace('breakout:', 'state:'))
        if '2x:' in line:
            yaml_content = yaml_content.replace(line, line.replace('2x:', 'up:'))
    return yaml_content

def process_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_content = file.read()

    modified_yaml = replace_breakout_with_state(yaml_content)

    with open(file_path, 'w') as file:
        file.write(modified_yaml)

if __name__ == "__main__":
    file_path = "T0-1_air.yaml"  # Replace with your actual YAML file path
    process_yaml_file(file_path)
