import argparse
import csv
from tabulate import tabulate
from collections import defaultdict

def get_average_ratings(file_paths: list):
    brands = defaultdict(lambda: [0.0, 0])
    for file_path in file_paths:
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                brand = row["brand"]
                rating = float(row["rating"])
                brands[brand][0] += rating
                brands[brand][1] += 1

    avg = {brand: round(s / c, 2) for brand, (s, c) in brands.items()}
    return avg

def save_report(file_path: str, data: dict):
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    with open(file_path, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["#", "brand", 'rating'])
        for i, (brand, rating) in enumerate(sorted_data, start=1):
            writer.writerow([i, brand, rating])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs="+", type=str, required=True)
    parser.add_argument('-r', '--report', type=str, required=True)
    args = parser.parse_args()

    averages = get_average_ratings(args.files)
    sorted_data = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    table = [[i+1, brand, rating] for i, (brand, rating) in enumerate(sorted_data)]
    headers = [" ", "brand", 'rating']
    print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f"))
    save_report(args.report, averages)

if __name__ == '__main__':
    main()