#!/bin/bash

sh PatricBrowserTools/PatricBrowserTools_Slurm.sh \
   -o Path/to/your/directory \
   -i data/Unique_Genome_IDs.txt \
    -f fna -c 90 -m 2 -report -l