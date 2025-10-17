import argparse
import csv
from tabulate import tabulate
from collections import defaultdict


def read_csv_files(file_paths: list):
    all_rows = []
    for path in file_paths:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            all_rows.extend(reader)
    return all_rows


def save_report(file_path: str, data: dict):
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    with open(file_path, "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([" ", "brand", 'value'])
        for i, (brand, value) in enumerate(sorted_data, start=1):
            writer.writerow([i, brand, value])


def print_report(data: dict):
    sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
    table = [[i+1, brand, value] for i, (brand, value) in enumerate(sorted_data)]
    headers = ["#", "Brand", "Value"]
    print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".2f"))


def aggregate_average_rating(rows):
    brands = defaultdict(lambda: [0.0, 0])
    for row in rows:
        brand = row["brand"]
        rating = float(row["rating"])
        brands[brand][0] += rating
        brands[brand][1] += 1
    return {brand: round(s / c, 2) for brand, (s, c) in brands.items()}

def aggregate_average_price(rows):
    brands = defaultdict(lambda: [0.0, 0])
    for row in rows:
        brand = row["brand"]
        price = float(row["price"])
        brands[brand][0] += price
        brands[brand][1] += 1
    return {brand: round(s / c, 2) for brand, (s, c) in brands.items()}


AGGREGATORS = {
    "rating": aggregate_average_rating,
    "price": aggregate_average_price,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--files', nargs="+", type=str, required=True)
    parser.add_argument('-r', '--report', type=str, required=True)
    parser.add_argument('-t', '--report-type', type=str, required=True, choices=AGGREGATORS.keys())
    args = parser.parse_args()

    rows = read_csv_files(args.files)
    data = AGGREGATORS[args.report_type](rows)

    print_report(data)
    save_report(args.report, data)

if __name__ == "__main__":
    main()