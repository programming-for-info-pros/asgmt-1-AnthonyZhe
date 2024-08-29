import csv

with open('2024_medalists_all.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
