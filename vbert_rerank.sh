#!/bin/bash
python3 cedr/rerank.py \--model vanilla_bert \--datafiles data/queries.tsv data/documents.tsv \--run data/top3 \--model_weights models/vbert/weights.p \--out_path models/vbert/test.run
