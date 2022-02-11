import csv


def write_csv_file(rows, field_names, csv_output_file_path):
    with open(csv_output_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for item in rows:
            writer.writerow(item)
