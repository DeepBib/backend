#!/bin/bash
python3 cedr/train.py \--model vanilla_sci_bert \--datafiles data/dummies/queries.tsv data/dummies/documents.tsv \--qrels data/dummies/qrels \--train_pairs data/dummies/qrels \--valid_run data/dummies/top3 \--model_out_dir models/sbert
