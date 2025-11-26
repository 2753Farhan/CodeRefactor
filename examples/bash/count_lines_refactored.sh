#!/bin/bash

# Refactored: use -exec with + to pass multiple files to wc, reducing process invocations
# This is functionally equivalent but much more efficient on many files

find . -type f -name "*.txt" -exec wc -l {} +
