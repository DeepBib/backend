import os

os.system("python3 cedr/rerank.py \--model vanilla_bert \--datafiles data/query.tsv data/documents.tsv \--run data/arxivRun \--model_weights models/vbert/weights.p") 
