
import csv

from scraper import get_profile_info

def get_csv(data, filename='leetcode_profile.csv'):

    if not data:
        print("data is not available")
        return


    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["username", "ranking", "easy", "medium", "hard", "total"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        if isinstance(data, dict):
            writer.writerow(data)
        
        elif isinstance(data, list):
            writer.writerows(data)

        else:
            print("Invalid data format - expected dict or list of dicts")
    



