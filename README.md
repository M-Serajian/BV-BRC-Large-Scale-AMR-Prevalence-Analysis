# Large-scale Analysis of Antimicrobial Resistance Prevalence in BV-BRC (Patric)

## Overview
This project involves a comprehensive analysis of antimicrobial resistance (AMR) prevalence, specifically focusing on Mycobacterium tuberculosis using data from the BV-BRC (Patric) database. The process includes data acquisition, analysis, and AMR prediction, all aimed at understanding and combating antimicrobial resistance more effectively.

### Steps Involved:

1. **Data Acquisition:** Downloading metadata of Mycobacterium tuberculosis from BV-BRC (Patric), including over 300,000 experiments on more than 27,000 isolates.
    - Data source: [BV-BRC (Patric)](https://www.bv-brc.org/)

2. **Metadata Analysis:** A detailed analysis of the metadata is conducted to gain insights and prepare the data for further processing.
    - Analysis Notebook: [Analyzing the metadata](https://github.com/M-Serajian/Scientific_reports_MTB_plus_plus/blob/main/patric_metadata_analisys/patric_metadata_analysis.ipynb)

3. **Data Retrieval:** Utilizing PatricBrowserTools for efficient data retrieval from the BV-BRC database.
    - Tool Link: [PatricBrowserTools](https://github.com/M-Serajian/PatricBrowserTools)

4. **Pre-processing of FASTA Files:** Processing the FASTA files using FASTATrimmer for optimal analysis readiness.
    - Tool Link: [FASTATrimmer](https://github.com/M-Serajian/FASTATrimmer)

5. **Predicting AMR:** Employing MTB++ for accurate prediction of antimicrobial resistance.
    - Tool Link: [MTB++](https://github.com/M-Serajian/MTB-plus-plus)

6. **Analyzing Results:** Post-prediction analysis to interpret and understand the implications of the findings.

## Contributing
We welcome contributions to this project. For details on how to contribute, please refer to the project's contribution guidelines.

## License
This project is licensed under [SPECIFY LICENSE]. For more information, please refer to the LICENSE file in the repository.
