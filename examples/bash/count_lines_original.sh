#!/bin/bash

# Original inefficient script: calls wc once for each file
# Find all .txt files and count lines in each
for file in $(find . -type f -name "*.txt"); do
    wc -l "$file"
done
