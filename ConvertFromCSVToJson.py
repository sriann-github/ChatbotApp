import csv
import json

def csv_to_json(csv_file, json_file):
    """Converts a CSV file to a JSON file."""

    data = []

    # Read the CSV file
    with open(csv_file, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)

    # Write the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    csv_file = r'D:\Learning-Valli\Azure\Data Files for Solutions\chatbot\10-21-Incidents\users_table.csv'  # Replace with your CSV file name
    json_file = r'D:\Learning-Valli\Azure\Data Files for Solutions\chatbot\10-21-Incidents\users_table.json'  # Replace with your desired JSON file name

    csv_to_json(csv_file, json_file)