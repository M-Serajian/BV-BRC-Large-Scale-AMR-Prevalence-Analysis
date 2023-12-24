#!/bin/bash
#SBATCH --job-name=$MTB++
#SBATCH --mail-type=ALL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=m.serajian@ufl.edu   # Where to send mail
#SBATCH --ntasks=1                       # Run a single task
#SBATCH --mem=1                       # Job Memory
#SBATCH --time=10:00:00                # Time limit hrs:min:sec
#SBATCH --array=1-10                 # Array range
#SBATCH --output=/home/m.serajian/share/MTB_Database/MTB++_logs/MTB++_%A_%a.log

RUN=$SLURM_ARRAY_TASK_ID
((RUN++))  #First line is for header of the csv file, that is why +1 is added
csv_file="/home/m.serajian/projects/Scientific_reports_MTB_plus_plus/data/Downloaded_genomes.csv"

genomes_directory="/home/m.serajian/share/MTB_Database/DV-BRC-Sientific-reports-Jan2024"
genome_id=$(sed -n "${RUN}p" $csv_file)


echo $RUN 
echo $genome_id


output_directory="/home/m.serajian/share/MTB_Database/MTB++_predictions"
ml python 

#python /home/m.serajian/projects/Scientific_reports_MTB_plus_plus/MTB-plus-plus/Mtb++.py -f $genomes_directory/$genome_id.fna -o $output_directory/$genome_id.csv

python /home/m.serajian/projects/test/MTB-plus-plus/Mtb++.py -f data/sample_genomes/ERR8665561.fasta -o ERR8665561.csv