#!/usr/bin/env python
## This script checks a certain key contents between 2 files
import sys
import argparse
from ruamel.yaml import YAML

parser = argparse.ArgumentParser(description='Compare YAML files certain key values.')
parser.add_argument('src', type=str,
                   help='Path to a source file')
parser.add_argument('dst', type=str,
                   help='Path to a destination file')
parser.add_argument('key', type=str,
                   help='yaml key to compare')
parser.add_argument('--v',action="store_true",
                   help='in depth key values comparison')


args = parser.parse_args()
src_file=open(args.src)
dst_file=open(args.dst)
yaml=YAML()
src_yaml=yaml.load(src_file)
dst_yaml=yaml.load(dst_file)
try:
  src_yaml[args.key]
except KeyError:
  print("{} does not contain {}".format(args.src,args.key))
else:
  try:
    dst_yaml[args.key]
  except KeyError:
    print("{} does not contain {}".format(args.dst,args.key))
  else:
    print("{} vs {} : {}".format(args.src,args.dst,(src_yaml[args.key] == dst_yaml[args.key])))
    if ((not (src_yaml[args.key] == dst_yaml[args.key])) and (args.v)):
      for subkey in src_yaml[args.key]:
        try:
          dst_yaml[args.key][subkey]
        except:
          print("{} is not present in {}".format(subkey,args.dst))
        else:
          if ( src_yaml[args.key][subkey] == dst_yaml[args.key][subkey] ):
            print("{} has equal value".format(subkey))
          else:
            print("{2} : {0} vs {1}".format(src_yaml[args.key][subkey],dst_yaml[args.key][subkey],subkey))
      for subkey in dst_yaml[args.key]:
        try:
          src_yaml[args.key][subkey]
        except:
          print("{} is not present in {}".format(subkey,args.src))

