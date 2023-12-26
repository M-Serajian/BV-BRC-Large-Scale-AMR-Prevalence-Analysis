#!/bin/bash
#SBATCH --job-name=Fasta_coreector
#SBATCH --mail-type=ALL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                       # Run a single task
#SBATCH --mem=1gb                        # Job Memory
#SBATCH --time=2:00:00               # Time limit hrs:min:sec
#SBATCH --array=1-100                 # Array range
#SBATCH --output=logs/"Fasta_coreector"_%A_%a.log


#Job array Id
RUN=${SLURM_ARRAY_TASK_ID:-1}
echo $RUN

INPUT_LIST=/home/m.serajian/projects/Scientific_reports_MTB_plus_plus/data/Downloaded_genomes.csv

Number_of_genomes=$(wc -l < "$INPUT_LIST")

# Calculate the number of lines each CPU should process (ceiling)
lines_per_cpu=274
echo $lines_per_cpu is allocated to each CPU

# Calculate the start and end lines for the current job
start_line=$(((SLURM_ARRAY_TASK_ID - 1) * lines_per_cpu + 1))
end_line=$((start_line + lines_per_cpu - 1))

if [ "$end_line" -ge "$total_lines" ]; then
    end_line="$(($Number_of_genomes - 1))"
fi
echo "starting line =" $start_line
echo "Ending line   =" $end_line

ml python

# Process lines in the specified interval
for ((line_num = $start_line; line_num <= $end_line; line_num++)); do

    INPUT_FILE=$(sed -n "${line_num}p" "$INPUT_LIST")

    echo "processing genome ID ${INPUT_FILE}, ${line_num}"
     
    python main.py $INPUT_FILE.fna


done


