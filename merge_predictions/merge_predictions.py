#!/usr/bin/env python
import os
import csv
import argparse


# ANSI color codes for print
red_color = "\033[91m"
blue_color = "\033[94m"
green_color = "\033[92m"
reset_color = "\033[0m"


def get_csv_files(data_directory):
    # Get a list of CSV files in the data directory
    csv_files = [file for file in os.listdir(data_directory) if file.lower().endswith('.csv')]

    if not csv_files:
        error_message = f"{red_color}No CSV files found in the data directory: {data_directory}. There are no MTB++ reports available.{reset_color}"
        print(error_message)
        raise FileNotFoundError(error_message)

    # Return base names without the '.csv' extension
    return [os.path.splitext(file)[0] for file in csv_files]

def validate_directories(data_directory, output_directory):
    # Validate data directory
    if not os.path.exists(data_directory):
        print(f"Error: Data directory '{data_directory}' does not exist.")
        exit(1)

    # Validate output directory
    if not os.path.exists(output_directory):
        print(f"Error: Output directory '{output_directory}' does not exist.")
        exit(1)


# Finding the reports of MTB++ 
def get_csv_files(data_directory):
    # Get a list of CSV files in the data directory
    csv_files = [file for file in os.listdir(data_directory) if file.lower().endswith('.csv')]

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in the data directory: {data_directory}. There are no MTB++ reports available.")

    return [os.path.splitext(file)[0] for file in csv_files]  # Remove '.csv' extension



def MTBpp_report(csv_file_path, model):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Iterate through rows
        for row in csv_reader:
            if row and row[0] == model:
                return row[1:]

    # Return None if the target value is not found
    return None


def process_mtb_results(data_directory, output_directory, input_data):
    # List to store data
    LR_predictions = []
    RF_predictions = []
    csv_header = ['Genome ID', 'Amikacin', 'Bedaquiline', 'Clofazimine', 'Delamanid', 'Ethambutol', 'Ethionamide', 
              'Isoniazid', 'Kanamycin', 'Levofloxacin', 'Linezolid', 'Moxifloxacin', 'Rifampicin', 'Rifabutin', 
              'RIA', 'AMG', 'FQS']
    
    LR_predictions.append(csv_header)
    RF_predictions.append(csv_header)

    # Iterate through Genome IDs in the input CSV file
    for genome_id in input_data:
        file_path = os.path.join(data_directory, f'{genome_id}.csv')

        if os.path.exists(file_path):
            LR_prediction=MTBpp_report(file_path,"Logistic Regression")
            LR_predictions.append([genome_id] + LR_prediction)
            
            RF_prediction=MTBpp_report(file_path,"Random Forest")
            RF_predictions.append([genome_id] + RF_prediction)

    # Write the consolidated data to a single output CSV file
    LR_output = 'Logistic Regression.csv'
    LR_output = os.path.join(output_directory, LR_output)
    with open(LR_output, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerows(LR_predictions)

    RF_output = 'Random Forest.csv'
    RF_output = os.path.join(output_directory, RF_output)
    with open(RF_output, 'w', newline='') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerows(RF_predictions)

    print(f"Report CSV files are available at: {output_directory}")



def main():
    # Argument parser
    parser = argparse.ArgumentParser(description='Process MTB++ results and create a consolidated CSV file.')
    parser.add_argument('-d', '--data-directory', required=True, help='Directory where the MTB++ results are stored.')
    parser.add_argument('-o', '--output-directory', required=True, help='Directory to save the consolidated CSV file.')
    args = parser.parse_args()

    # Validate directories
    validate_directories(args.data_directory, args.output_directory)

    # finding the reports
    input_data = get_csv_files(args.data_directory)
    # Process MTB++ results and create the consolidated CSV file
    process_mtb_results(args.data_directory, args.output_directory, input_data)


if __name__ == "__main__":
    main()
