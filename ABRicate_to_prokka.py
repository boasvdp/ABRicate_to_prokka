#!/usr/bin/env python3

import re
import argparse

parser = argparse.ArgumentParser(description='Get Prokka tags for ABRicate hits')

parser.add_argument("-a", "--abricate", dest="abricate", help="input ABRicate file", metavar="ABRICATE FILE", type=str)
parser.add_argument("-p", "--prokka", dest="prokka", help="input prokka file", metavar="PROKKA FILE", type=str)

args = parser.parse_args()

abr = open(args.abricate, "r")

for line in abr.readlines():
  OUT = '-'
  if line.startswith("#"):
    continue
  contig = line.split('\t')[1]
  start = line.split('\t')[2]
  end = line.split('\t')[3]
  name = line.split('\t')[5]
  for line2 in open(args.prokka, "r").readlines():
    if line2.startswith('##FASTA'):
      break
    if line2.startswith('#'):
      continue
    if (line2.split('\t')[0] == contig) & ((int(line2.split('\t')[3]) - int(start)) < 10) & ((int(line2.split('\t')[4]) - int(end)) < 10):
      OUT = re.compile('[A-Z]{8}_[0-9]{5}').findall(line2)
  print(name, OUT[0], sep = '\t')
