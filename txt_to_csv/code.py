
import csv

def txt_to_csv(txt_file_path, csv_file_path, delimiter=','):
    with open(txt_file_path, 'r') as txt_file:
        lines = txt_file.readlines()

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        for line in lines:
            row = line.strip().split(delimiter)
            writer.writerow(row)

# Example usage:
txt_file_path = r"E:\arcgis\Gridpoints.txt.txt"
csv_file_path = r"E:\arcgis\grid_point.csv"
txt_to_csv(txt_file_path, csv_file_path, delimiter=',')
