import os
import argparse
import sys
sys.path.append('cedr')

import data

def main_cli():
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
    os.system("python3 cedr/rerank.py \--model vanilla_bert \--datafiles data/query.tsv data/documents.tsv \--run data/arxivRun \--model_weights models/vbert/weights.p --out_path models/vbert/test.run") 

if __name__ == '__main__':
    main_cli()
