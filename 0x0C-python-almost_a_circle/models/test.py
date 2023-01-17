#!/usr/bin/python3
import csv

with open("Rectangle.csv", "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
