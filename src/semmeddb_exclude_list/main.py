"""Main python file."""
import csv

from src.semmeddb_exclude_list.download import download_file

def convert_input_to_output():

    type_exclusion_filepath = download_file(target_directory_name="SEMMEDDB",
                             url="https://docs.google.com/spreadsheets/d/1c1gx0Jgm9rJUOXcQhBtZgvx50Cvz1-jh0DdGtg1zcd8/export?gid=1662224030&format=tsv&sheet=semantic_types_exclusions")
    # Split the input data by lines
    domain_exclusion_filepath = download_file(target_directory_name="SEMMEDDB_DOMAIN",
                                                 url="https://docs.google.com/spreadsheets/d/1c1gx0Jgm9rJUOXcQhBtZgvx50Cvz1-jh0DdGtg1zcd8/export?gid=1129435652&format=tsv&sheet=semantic_types_exclusions")

    # Split the input data by lines
    range_exclusion_filepath = download_file(target_directory_name="SEMMEDDB_RANGE",
                                                 url="https://docs.google.com/spreadsheets/d/1c1gx0Jgm9rJUOXcQhBtZgvx50Cvz1-jh0DdGtg1zcd8/export?gid=2099428392&format=tsv&sheet=semantic_types_exclusions")


    print("type_exclusion_filepath", type_exclusion_filepath)
    print("domain_exclusion_filepath", domain_exclusion_filepath)
    print("range_exclusion_filepath", range_exclusion_filepath)

    parsed_output = []
    parsed_output.append(("SEMMEDDB Subject Code",
                          "SEMMEDDB Subject T code",
                          "SEMMEDDB Predicate",
                          "SEMMEDDB Object Code",
                          "SEMMEDDB Object T code",
                          "Notes"))

    with open(type_exclusion_filepath, 'r', newline='', encoding='utf-8') as file:
        for line in file:
            line = line.split("\t")
            if line[0].startswith("SEMMEDDB"):
                continue
            if len(line) < 6:
                print("length", len(line))
                continue
            if line[6] in ["Exclude", "exclude"]:
                exclude_line1 = (line[0], line[1], line[6], "", "", "semantic type exclusion")
                exclude_line_2 = ("", "", line[6], line[0], line[1])
                parsed_output.append(exclude_line1)
                parsed_output.append(exclude_line_2)


    with open(domain_exclusion_filepath, 'r', newline='', encoding='utf-8') as file:
        for line in file:
            line = line.split("\t")
            if line[6] != "0":
                exclude_line1 = ("", line[1], line[3], "", "", "Domain exclusion")
                parsed_output.append(exclude_line1)

    with open(range_exclusion_filepath, 'r', newline='', encoding='utf-8') as file:
        for line in file:
            line = line.split("\t")
            print(line)
            if line[6] != "0":
                exclude_line1 = ("", "", line[3], "", line[1], "Range exclusion")
                parsed_output.append(exclude_line1)

    write_tsv_file(parsed_output, "SEMMEDDB_exclude_list.tsv")


def write_tsv_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as tsvfile:
        for row in data:
            tsvfile.write('\t'.join(map(str, row)) + '\n')
    print(f'TSV file "{filename}" has been created.')


if __name__ == "__main__":
    parsed_output = convert_input_to_output()


