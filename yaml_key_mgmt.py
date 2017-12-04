#!/usr/bin/env python
import ruamel.yaml
import re
import sys
import argparse
parser = argparse.ArgumentParser(description='Manage certain key from yaml files. Just lists key value by default')
parser.add_argument('src', type=str,
                   help='Source yaml file to change')
parser.add_argument('key', type=str,
                   help='yaml key')
parser.add_argument('--remove', action="store_true",
                   help='remove requested key')

args = parser.parse_args()
yamlfile=args.src;
keytoexpunge=args.key
remove=args.remove
config=ruamel.yaml.load(open(yamlfile),Loader=ruamel.yaml.RoundTripLoader,preserve_quotes=True)
try:
  config[keytoexpunge]
except KeyError:
  print("No key like {} found in {}".format(keytoexpunge,yamlfile))
else:
  if remove:
    del config[keytoexpunge]
    config.update(dict.fromkeys([key for key in config if config[key] == None],'~'))
    with open(yamlfile,'w') as yaml_file:
      yaml_file.write(re.sub('\'~\'','~',ruamel.yaml.dump(config, Dumper=ruamel.yaml.RoundTripDumper)))
  else:
    ruamel.yaml.dump(config[keytoexpunge], sys.stdout, Dumper=ruamel.yaml.RoundTripDumper)
