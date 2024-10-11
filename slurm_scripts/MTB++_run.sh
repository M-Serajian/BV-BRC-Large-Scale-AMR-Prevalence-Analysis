#!/bin/bash
#SBATCH --job-name=MTB++
#SBATCH --mail-type=ALL                # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                     # Run a single task
#SBATCH --mem=1gb                      # Job Memory
#SBATCH --time=10:00:00                # Time limit hrs:min:sec
#SBATCH --array=1-10                 # Array range
#SBATCH --output=MTB_Database/MTB++_logs/MTB++_%A_%a.log

RUN=$SLURM_ARRAY_TASK_ID
RUN=$((RUN ++))
echo $RUN 
#First line is for header of the csv file, that is why +1 is added
csv_file="Scientific_reports_MTB_plus_plus/data/Downloaded_genomes.csv"

genomes_directory="/MTB_Database/DV-BRC_corrected" 
genome_id=$(sed -n "${RUN}p" $csv_file)

echo $genome_id

output_directory="MTB_Database/MTB++_predictions"

module load python 

python /MTB-pipeline/Mtb++.py -f $genomes_directory/$genome_id.fna -o $output_directory/$genome_id.csv
