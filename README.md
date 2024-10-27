
# Large-scale Analysis of Antimicrobial Resistance Prevalence in BV-BRC (Patric) database

## Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Steps Involved](#steps-involved)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project is dedicated to understanding antimicrobial resistance (AMR) in *Mycobacterium Tuberculosis* by leveraging data from the BV-BRC (previously known as Patric) database. Our work aims to shed light on the prevalence and patterns of AMR, providing useful insights to the scientific community and supporting future research and treatment strategies.

## Overview
We take a systematic approach to AMR analysis, incorporating large-scale data retrieval, metadata analysis, and predictive modeling. By exploring the rich metadata available and applying advanced tools, this project aims to contribute to the ongoing efforts in combating drug resistance.

### Steps Involved

1. **Clone the project:**
   ```bash
   git clone https://github.com/M-Serajian/BV-BRC-Large-Scale-AMR-Prevalence-Analysis.git
   cd BV-BRC-Large-Scale-AMR-Prevalence-Analysis
   git submodule update --init --recursive
   ```

2. **Data Acquisition:** Download the metadata of *Mycobacterium tuberculosis* from BV-BRC, including over 27,000 isolates that have been used in over 300,000 MTB antimicrobial resistance experiments.  
    - Data source: [BV-BRC](https://www.bv-brc.org/)

3. **Metadata Analysis:** Perform a detailed analysis of the metadata to extract valuable insights and prepare the data for further processing. Approximately 27,000 unique isolate IDs were found, and a list was created to retrieve them from the BV-BRC database. Non-human isolates were excluded from further analysis.  
    - Analysis Notebook: [Analyzing the metadata](https://github.com/M-Serajian/BV-BRC-Large-Scale-AMR-Prevalence-Analysis/blob/main/BV-BRC_metadata_analysis/BV-BRC_metadata_analysis.ipynb)

4. **Data Retrieval:** Use BV-BRC-BrowserTools for efficient data retrieval from the BV-BRC database. As part of this project, we developed a tool to retrieve over 27,000 isolates in under an hour.  
    - Tool Link: [BV-BRC-BrowserTools](https://github.com/M-Serajian/BV-BRC-BrowserTools)

   ```bash
   cd BV-BRC-BrowserTools
   sh BV-BRC-BrowserTools_Slurm.sh [options]
   ```

   **Options:**
   - **`-o GENOMES_SAVING_DIRECTORY`**  
     Specify the directory where the genomic data from BV-BRC will be stored. This directory must have more than 1TB of available space as the genomic data can be very large.

   - **`-i GENOME_ID_TEXT_FILE_DIRECTORY`**  
     Provide the directory to the text file that contains genome IDs collected from a previous step. These genome IDs will be used for further analysis.

   - **`-f FILE_TYPE`**  
     The format of the genomic data to be downloaded. For example, use `fna` for FASTA format.

   **Example Command:**
   ```bash
   sh BV-BRC-BrowserTools_Slurm.sh -o /path/to/genomes_directory -i /path/to/genome_ids_directory -f fna
   ```

5. **Predicting AMR:** Use MTB++ for accurate prediction of antimicrobial resistance.  
    - Tool Link: [MTB++](https://github.com/M-Serajian/MTB-Pipeline)

   ```bash
   cd ..
   cd MTB-Pipeline
   sh setup.sh
   ```

   Running MTB++:
   ```bash
   python Mtb++.py -f FASTAfile -o Output.csv
   ```
MTB++ fully supports parallel execution. For optimal workflow, we recommend storing the output predictions in a designated directory, such as `MTB++_output_directory`, with each file saved as a uniquely named CSV. This structure ensures efficient processing in the subsequent steps, particularly when using the MTB++_Report_Consolidation method, which is designed to streamline report aggregation within MTB++.

6. **Analyzing Results:** Interpret the results from the AMR prediction and compile them into a comprehensive CSV file for further analysis of all isolates.
```bash
ruby MTB++_Report_Consolidation.rb -d [DATA_DIRECTORY] -o [OUTPUT_DIRECTORY]
```
**Options:**
   - **`-DATA_DIRECTORY`**
     DATA_DIRECTORY is the directory where the predictions of MTB++ are stored; it is the same as `MTB++_output_directory` which was defined in the previous step. 
   - **`-o OUTPUT_DIRECTORY`**  
     The output directory will contain consolidated data, generating two CSV files: one for logistic regression and one for random forest. These files will present MTB++ predictions for each unique genome ID, including the corresponding organized antibiotic resistance phenotypes.

## Getting Started
These instructions will help you set up the project on your local machine for development and testing.

### Dependencies
- [Python](https://www.python.org/) 3.0+ (3.6+ recommended)
   - [sklearn](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1-2) (Version 1.1.2)
   - [joblib](https://joblib.readthedocs.io/en/stable/) (Pre-installed with Python 3+)
- [CMake](https://cmake.org/) (tested on v3.26.4)
- [GCC](https://gcc.gnu.org/) (9.3.3 recommended)

Follow the [MTB++ installation instructions](https://github.com/M-Serajian/MTB-plus-plus/tree/main#installation) for further setup.

## Contributing
We welcome contributions to this project. Please refer to the project's contribution guidelines for details on how to contribute.

## License
This project is licensed under [SPECIFY LICENSE]. For more information, please refer to the LICENSE file in the repository.
