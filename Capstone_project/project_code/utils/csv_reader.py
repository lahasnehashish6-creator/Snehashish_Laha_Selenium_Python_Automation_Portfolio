import csv


def read_test_data():
    with open("data/test_data.csv", newline="") as file:
        return list(csv.DictReader(file))