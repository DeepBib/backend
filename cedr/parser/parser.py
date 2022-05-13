#!/usr/bin/python

import re
import json
import csv
import pandas as pd
import numpy as np

import sys

jsontest = sys.argv[1]
query = sys.argv[2]

def spl_chars_removal(str):   
    ##[0-9\]
    str = re.sub("\n","",str)
    return str

with open("documents.tsv", "w") as fichier:
  cpt = 0
  for ele in jsontest :
    cpt+=1
    sum = spl_chars_removal(ele.get("summary")[0])
    fichier.write("doc "+str(cpt)+" "+sum+"\n")
    
with open("queries.tsv", "w") as fichier:
    fichier.write("query "+"1 "+query+"\n")
    