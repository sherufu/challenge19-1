import csv

lists = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"],
    ["Training Day", "Man on Fire", "Flight"]
    ]

with open("challenge9-3.csv", "w", encoding="utf-8", newline='') as f:
    w = csv.writer(f, delimiter=',')
    for l in lists:
        w.writerow(l)
