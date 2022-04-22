#!/bin/bash
python3 cedr/train.py \--model cedr_pacrr \--datafiles data/queries.tsv data/documents.tsv \--qrels data/qrels \--train_pairs data/train_pairs \--valid_run data/top3 \--initial_bert_weights models/vbert/weights.p \--model_out_dir models/cedrpacrr
