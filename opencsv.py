# -*- coding: utf-8 -*-
import csv
import os

base=os.path.basename("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv")

def openCSV(table):
    with open("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == table:
                return row[1]
                break;

print openCSV("cfg_billing_id")
