# yaml_scripts
Various scripts to manage yaml files

List/Remove certain key
./yaml_key_mgmt.py -h
usage: yaml_key_mgmt.py [-h] [--remove] src key

Manage certain key from yaml files. Just lists key value by default

positional arguments:
  src         Source yaml file to change
  key         yaml key

optional arguments:
  -h, --help  show this help message and exit
  --remove    remove requested key

Compare key value for 2 eyaml files:
yaml_similarity.py  -h
usage: yaml_similarity.py [-h] [--v] src dst key

Compare YAML files certain key values.

positional arguments:
  src         Path to a source file
  dst         Path to a destination file
  key         yaml key to compare

optional arguments:
  -h, --help  show this help message and exit
  --v         in depth key values comparison
