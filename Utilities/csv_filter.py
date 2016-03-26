__author__ = 'Bharat'

import csv


with open('Restaurant.csv', 'rb') as inp, open('phx.csv', 'wb') as out:
    writer = csv.writer(out)
    count = 0
    for row in csv.reader(inp):
        if row[58] == 'Phoenix' or row[58] == 'Pheonix' or row[58] == 'Phoenix Sky Harbor Center' or count == 0:
            writer.writerow(row)
            count += 1
