#!/bin/bash
set -euo pipefail

curl -L "https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz" -o bundle.tar.gz

tar -xzf bundle.tar.gz

awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

ROW_COUNT=$(($(wc -l < cleaned.csv) - 1))


echo "$ROW_COUNT"

tar -czf converted-archive.tar.gz cleaned.csv
