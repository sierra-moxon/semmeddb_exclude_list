"""Main python file."""
import csv

from src.semmeddb_exclude_list.download import download_file

def convert_input_to_output():

    type_exclusion_filepath = download_file(target_directory_name="SEMMEDDB",
                             url="https://docs.google.com/spreadsheets/d/1c1gx0Jgm9rJUOXcQhBtZgvx50Cvz1-jh0DdGtg1zcd8/gviz/tq?tqx=out:csv&sheet=semantic_types_exclusions")
    # Split the input data by lines


    print("type_exclusion_filepath", type_exclusion_filepath)

    with open(type_exclusion_filepath, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row
        parsed_data = [row for row in reader]

    # Process the remaining lines
    for line in parsed_data:
        print("line", line)
        # Split each line by tabs

        # Extract the excluded semantic types
        excluded_types = []
        output_data = []

    return output_data


if __name__ == "__main__":
    convert_input_to_output()

