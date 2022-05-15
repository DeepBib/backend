#!/usr/bin/python

import os
import argparse
import re
import sys
import json
import data

query = sys.argv[1]
jsonPath = sys.argv[2]

## Les prints c'est pour debug avec le server
 
print("--------------Pyhton running------------") 
def spl_chars_removal(str):
    str = re.sub("\n","",str)
    return str


def parser(name,jsonD) :
    print("------Python--parser------") 
    with open("./../cedr/parser/documents.tsv", "w") as fichier:
        cpt = 0
        for ele in jsonD :
            cpt+=1
            sum = spl_chars_removal(ele.get("summary")[0])
            fichier.write("doc "+str(cpt)+" "+sum+"\n")
        with open("./../cedr/parser/queries.tsv", "w") as fichier:
            fichier.write("query "+"1 "+name+"\n")
    print("------Python--parser-END-----") 
  
def ranker():
    print("------Python--ranker---START---") 
    parser = argparse.ArgumentParser('generating qrels and train pairs')
    parser.add_argument('--datafiles', type=argparse.FileType('rt'), nargs='+')
    args = parser.parse_args()
    dataset = data.read_datafiles(args.datafiles)

    # formatting doc list & giving very approximate relevance judgments based on retrieved order
    f  = open("data/arxivRun","w")
    for docnumber in dataset[1] :
       f.write("0	Q0	"+docnumber+"	"+docnumber+"	10.0	run\n")
    f.close()

    # executing rerank model & printing results
    # for the test we set the path for query and document in parser folder
    os.system("python3 cedr/rerank.py \--model vanilla_bert \--datafiles parser/query.tsv parser/documents.tsv \--run data/arxivRun \--model_weights models/vbert/weights.p --out_path models/vbert/test.run") 
    print("------Python--ranker---END---") 

def score():
    print("To be done add key score to each json element  and write json file with the new value")
   
def main_cli(name,jsonD):
    parser(name,jsonD)
    ranker()
      
            
if __name__ == '__main__':
    print("------Python--Main begin------") 
    
    jsonDoc = open(jsonPath,)
    jsonData = json.load(jsonDoc)
    jsonDoc.close()
    main_cli(query,jsonData)
    print("------Python--Main end------") 
    
    
    
print("--------------Pyhton Ending------------") 
