#!/bin/bash
date;hostname
echo "The directory in which Patric_genome_downloader was run is: "
echo $(pwd)

cpus=100
Address_to_genome_id_text_file="/home/m.serajian/projects/Scientific_reports_MTB_plus_plus/data/Downloaded_genomes.csv"
genomes_root_address="/home/m.serajian/share/MTB_Database/DV-BRC_corrected/"

Number_of_genomes=$(awk 'END{print NR}' "$Address_to_genome_id_text_file")
echo "Number of genomes to be corrected:" $Number_of_genomes

slurm_script_address="MTB++_generative_slurm.sh"
Main_job_action_name=MTB++

cat << EOF > ${slurm_script_address}
#!/bin/bash
#SBATCH --job-name=${Main_job_action_name}
#SBATCH --mail-type=ALL            # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                       # Run a single task
#SBATCH --mem=1gb                        # Job Memory
#SBATCH --time=2:00:00               # Time limit hrs:min:sec
#SBATCH --array=1-${cpus}                 # Array range
#SBATCH --output=/home/m.serajian/share/MTB_Database/MTB++_logs/"$Main_job_action_name"_%A_%a.log


#Job array Id
RUN=\${SLURM_ARRAY_TASK_ID:-1}
echo \$RUN

INPUT_LIST=${Address_to_genome_id_text_file}
genomes_root_address=${genomes_root_address}
output_directory="/home/m.serajian/share/MTB_Database/MTB++_predictions"

Number_of_genomes=\$(wc -l < "\$INPUT_LIST")

# Calculate the number of lines each CPU should process (ceiling)
lines_per_cpu=$(awk -v total="$Number_of_genomes" -v cpus="$cpus" 'BEGIN { print int((total + cpus - 1) / cpus) }')
echo \$lines_per_cpu is allocated to each CPU

# Calculate the start and end lines for the current job
start_line=\$(((SLURM_ARRAY_TASK_ID - 1) * lines_per_cpu + 1))
end_line=\$((start_line + lines_per_cpu - 1))

if [ "\$end_line" -ge "\$total_lines" ]; then
    end_line="\$((\$Number_of_genomes - 1))"
fi
echo "starting line =" \$start_line
echo "Ending line   =" \$end_line

ml python

# Process lines in the specified interval
for ((line_num = \$start_line; line_num <= \$end_line; line_num++)); do

    INPUT_FILE=\$(sed -n "\${line_num}p" "\$INPUT_LIST")
    
    python /home/m.serajian/projects/Scientific_reports_MTB_plus_plus/MTB-plus-plus/Mtb++.py -f \$genomes_root_address/\$INPUT_FILE.fna -o \$output_directory/\$INPUT_FILE.csv

done


EOF

sbatch ${slurm_script_address}

echo ${Main_job_action_name} is submitted!
