import csv

with open('data.csv','r') as data_file:
    csv_reader = csv.reader(data_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)