import csv

from main import (
    read_csv_files,
    aggregate_average_rating,
    aggregate_average_price,
    save_report
)

def test_aggregate_average_rating(tmp_path):
    file = tmp_path / "ratings.csv"
    file.write_text("brand,rating\nApple,4.5\nSamsung,3.0\nApple,5.0\n")
    rows = read_csv_files([str(file)])
    result = aggregate_average_rating(rows)
    assert result == {"Apple": 4.75, "Samsung": 3.0}

def test_aggregate_average_price(tmp_path):
    file = tmp_path / "prices.csv"
    file.write_text("brand,price\nApple,100\nSamsung,200\nApple,300\n")
    rows = read_csv_files([str(file)])
    result = aggregate_average_price(rows)
    assert result == {"Apple": 200.0, "Samsung": 200.0}

def test_save_report(tmp_path):
    data = {"Apple": 4.75, "Samsung": 3.0}
    report_file = tmp_path / "report.csv"

    save_report(str(report_file), data)

    with open(report_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == [" ", "brand", "value"]
    assert rows[1] == ["1", "Apple", "4.75"]
    assert rows[2] == ["2", "Samsung", "3.0"]