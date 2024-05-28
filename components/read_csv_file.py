import csv

def read_csv_file(file_name):
    with open(file_name, mode="r", newline="") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [line for line in csv_reader]
    return data