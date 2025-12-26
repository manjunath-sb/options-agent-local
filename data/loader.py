import csv
from pathlib import Path

def load_company_snapshot():
    file_path = Path(__file__).parent / 'tcs_snapshot.csv'

    # Change 'utf-8' to 'utf-8-sig' to handle BOM if present
    with open(file_path, newline="", encoding= 'utf-8-sig') as csvfile:
        # This strips whitespace from every key and value automatically
        reader = csv.DictReader((line.replace('\0', '') for line in csvfile))
        rows = [{k.strip(): v.strip() for k, v in row.items()} for row in reader]

    
    if len(rows) != 1:
        raise ValueError("tcs_snapshot.csv must contain exactly one row")

    return rows[0]

""" Earlier version of the function without BOM handling and whitespace stripping
    def load_company_snapshot():

    file_path = Path(__file__).parent / 'data' / 'tcs_snapshot.csv'



    with open(file_path, newline="", encoding='utf-8') as csvfile:

        reader = csv.DictReader(csvfile)

        rows = list(reader) """