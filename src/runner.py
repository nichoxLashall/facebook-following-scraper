thonimport json
import os
import sys
from extractors.facebook_parser import FacebookParser
from outputs.exporters import DataExporter

def run_scraper(profile_url, max_items, output_format):
    try:
        facebook_parser = FacebookParser(profile_url, max_items)
        data = facebook_parser.scrape_following_data()

        exporter = DataExporter(output_format)
        exporter.export(data)

    except Exception as e:
        print(f"Error occurred during scraping: {e}")
        sys.exit(1)

if __name__ == "__main__":
    profile_url = sys.argv[1]  # Facebook profile URL
    max_items = int(sys.argv[2])  # Max items to scrape
    output_format = sys.argv[3]  # Desired output format (json, csv, etc.)
    
    run_scraper(profile_url, max_items, output_format)