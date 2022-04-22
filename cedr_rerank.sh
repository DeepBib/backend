#!/bin/bash
python3 cedr/rerank.py \--model cedr_pacrr \--datafiles data/queries.tsv data/documents.tsv \--run data/top3 \--model_weights models/cedrpacrr/weights.p \--out_path models/cedrpacrr/test.run
