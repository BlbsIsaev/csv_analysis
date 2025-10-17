import csv
from main import get_average_ratings, save_report

def test_get_average_ratings(tmp_path):
    file = tmp_path / "ratings.csv"
    file.write_text("brand,rating\nApple,4.5\nSamsung,3.0\nApple,5.0\n")

    result = get_average_ratings([str(file)])
    assert result == {"Apple": 4.75, "Samsung": 3.0}

def test_save_report(tmp_path):
    data = {"Apple": 4.75, "Samsung": 3.0}
    report_file = tmp_path / "report.csv"

    save_report(str(report_file), data)

    with open(report_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["#", "brand", "rating"]
    assert rows[1] == ["1", "Apple", "4.75"]
    assert rows[2] == ["2", "Samsung", "3.0"]