import csv

code = "utf-8"
#code = "cp932"

lists = [
    ["トップガン", "リスキービジネス", "マイノリティリポート"],
    ["タイタニック", "レヴナント", "インセプション"],
    ["トレーニングデイ", "マン・オン・ファイア", "フライト"]
    ]

with open("challenge9-4.csv", "w", encoding=code, newline='') as f:
    w = csv.writer(f, delimiter=',')
    for l in lists:
        w.writerow(l)
