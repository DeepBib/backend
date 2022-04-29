import os
import sys
import argparse
import subprocess
import random
import tempfile
from tqdm import tqdm
import torch
import modeling
import data
import pytrec_eval
from statistics import mean
from collections import defaultdict

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




    #train_pairs = data.read_pairs_dict(args.train_pairs)
    #valid_run = data.read_run_dict(args.valid_run)

    #if args.initial_bert_weights is not None:
    #    model.load(args.initial_bert_weights.name)
    #os.makedirs(args.model_out_dir, exist_ok=True)
    # we use the same qrels object for both training and validation sets
    # main(model, dataset, train_pairs, qrels, valid_run, qrels, args.model_out_dir)

if __name__ == '__main__':
    main_cli()
