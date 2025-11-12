thonimport json
import csv
import os

class DataExporter:
    def __init__(self, output_format):
        self.output_format = output_format

    def export(self, data):
        if self.output_format == "json":
            self.export_to_json(data)
        elif self.output_format == "csv":
            self.export_to_csv(data)
        else:
            raise ValueError(f"Unsupported format: {self.output_format}")

    def export_to_json(self, data):
        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def export_to_csv(self, data):
        with open('output.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)