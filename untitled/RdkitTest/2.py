#! /usr/bin/python
# coding: utf-8

import csv
import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Chem import rdFreeSASA
from rdkit.Chem.Scaffolds import MurckoScaffold

#csvFile = open('D:\\Work\\111111111.csv','rt', newline='', encoding='utf-8', errors='ignore')
filename = 'D:\\Work\\cmnpd.csv'
'''
reader = pd.read_csv(filename)
print(reader)
'''
a = 0
data = []
with open(filename,"r+",encoding="utf-8") as f:
    reader=csv.reader(f)
    rows = [row for row in reader]

print(rows)
rowlen = len(rows)
print(rowlen)
for line in rows:
    if a!=0:
        a = line[0]


print(rows[0])
print(rows[1])
print(rows[1][0])

'''
data = []
#headers = next(csvFile)
for line in reader:
    data.append(line)
print(data)
'''