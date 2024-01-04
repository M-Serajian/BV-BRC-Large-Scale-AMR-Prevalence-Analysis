# Large-scale Analysis of Antimicrobial Resistance Prevalence in BV-BRC (Patric)

## Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Steps Involved](#steps-involved)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project focuses on the critical analysis of antimicrobial resistance (AMR) in Mycobacterium tuberculosis, leveraging the comprehensive data available through the BV-BRC (Patric) database. It aims to provide insights into the prevalence and patterns of AMR, contributing to the broader scientific understanding and informing future research and treatment strategies.

## Overview
In this project, we undertake a systematic approach to analyze AMR prevalence. Our methodology encompasses the acquisition and analysis of extensive metadata, utilization of specialized tools for data retrieval and processing, and advanced predictive modeling techniques to interpret our findings.

### Steps Involved

1. **Data Acquisition:** Downloading metadata of Mycobacterium tuberculosis from BV-BRC (Patric), including over 300,000 experiments on more than 27,000 isolates.
    - Data source: [BV-BRC (Patric)](https://www.bv-brc.org/)

2. **Metadata Analysis:** Conducting a detailed analysis of the metadata to extract valuable insights and prepare the data for further processing.
    - Analysis Notebook: [Analyzing the metadata](https://github.com/M-Serajian/Scientific_reports_MTB_plus_plus/blob/main/patric_metadata_analisys/patric_metadata_analysis.ipynb)

3. **Data Retrieval:** Employing PatricBrowserTools for efficient data retrieval from the BV-BRC database.
    - Tool Link: [PatricBrowserTools](https://github.com/M-Serajian/PatricBrowserTools)

4. **Pre-processing of FASTA Files:** Using FASTATrimmer to process the FASTA files for optimal analysis readiness.
    - Tool Link: [FASTATrimmer](https://github.com/M-Serajian/FASTATrimmer)

5. **Predicting AMR:** Using MTB++ for accurate prediction of antimicrobial resistance.
    - Tool Link: [MTB++](https://github.com/M-Serajian/MTB-plus-plus)

6. **Analyzing Results:** Interpreting and understanding the implications of the findings from the AMR prediction.


## Getting Started
These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Dependencies
* [python](https://www.python.org/) 3.0+ (3.6+ recommended)
    - [sklearn](https://scikit-learn.org/stable/whats_new/v1.1.html#version-1-1-2) (Version 1.1.2) 
    - [joblib](https://joblib.readthedocs.io/en/stable/) (Pre-exists on python3+)
* [Cmake](https://cmake.org/)(tested on v3.26.4)
* [GCC](https://gcc.gnu.org/) (9.3.3 recommended)


## Contributing
We welcome contributions to this project. For details on how to contribute, please refer to the project's contribution guidelines.

## License
This project is licensed under [SPECIFY LICENSE]. For more information, please refer to the LICENSE file in the repository.
