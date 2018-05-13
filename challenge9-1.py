import csv

with open("challenge8-1.py", "r", encoding="utf-8") as f:
    r = csv.reader(f)
    for row in r:
        print(row)
