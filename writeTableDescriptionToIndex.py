import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

def getTableDescription(table):
    with open("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == table:
                return row[1]
                break;


def writeToHTML():

    source = "Data/settlement/index.html"
    with open(source) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    tables = soup.find_all('table')
    table_list = tables[3]

    table_names = table_list.find_all('a')

    for table in table_names:
        desc = getTableDescription(table.string)
        mother_table = table.parent.parent
        comment_section = mother_table.find_all("td", class_="comment detail")
        for c in comment_section:
            c.string = desc

    with open("Result/settlement_table_desc/index.html","w") as file:
        file.write(str(soup))

    print "Done writing table description to index.html"



writeToHTML();