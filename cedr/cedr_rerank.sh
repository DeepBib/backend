#!/bin/bash
python3 cedr/rerank.py \--model cedr_pacrr \--datafiles data/query.tsv data/documents.tsv \--run data/arxivRun \--model_weights models/cedrpacrr/weights.p \--out_path models/cedrpacrr/test.run
