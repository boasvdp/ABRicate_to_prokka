#!/usr/bin/env python3

import re
import argparse

parser = argparse.ArgumentParser(description='Get Prokka tags for ABRicate hits')

parser.add_argument("-a", "--abricate", dest="abricate", help="input ABRicate file", metavar="ABRICATE FILE", type=str)
parser.add_argument("-p", "--prokka", dest="prokka", help="input prokka file", metavar="PROKKA FILE", type=str)

args = parser.parse_args()

with open(args.abricate, "r") as abr:
  abr_lines = abr.readlines()

with open(args.prokka, "r") as prok:
  prok_lines = prok.readlines()

for abr_line in abr_lines:
  OUT = '-'
  if abr_line.startswith("#"):
    continue
  contig = abr_line.split('\t')[1]
  start = int(abr_line.split('\t')[2])
  end = int(abr_line.split('\t')[3])
  name = abr_line.split('\t')[5]
  for prok_line in prok_lines:
    if prok_line.startswith('##FASTA'):
      break
    if prok_line.startswith('#'):
      continue
    if (prok_line.split('\t')[0] == contig):
      prok_start = int(prok_line.split('\t')[3])
      prok_end = int(prok_line.split('\t')[4])
      if ((start <= prok_start) & (end > prok_start)) | ((prok_start <= start) & (start < prok_end)):
        OUT = re.compile('[A-Z]{8}_[0-9]{5}').findall(prok_line)
  print(name, OUT[0], sep = '\t')
