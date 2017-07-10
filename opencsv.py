# -*- coding: utf-8 -*-
import csv
import os

base=os.path.basename("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv")

with open("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        print row
