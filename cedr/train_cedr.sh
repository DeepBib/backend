#!/bin/bash
python3 cedr/train.py \--model cedr_pacrr \--datafiles data/dummies/queries.tsv data/dummies/documents.tsv \--qrels data/dummies/qrels \--train_pairs data/dummies/train_pairs \--valid_run data/dummies/top3 \--initial_bert_weights models/vbert/weights.p \--model_out_dir models/cedrpacrr
