import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

def getDescription(field):
    with open("Result/settlement_csv/cfg_billing_id.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0]==field:
                return row[1]


def writeToHTML(path):
    base=os.path.basename(path)
    with open(path) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    tables = soup.find_all('table')
    data_table = tables[5]

    table = data_table.find('tbody')

    rows = table.find_all('tr')


    for row in rows:
        field = row.contents[1].string
        comment_section = row.find_all("td", class_="comment detail")
        for r in comment_section:
            r.string = getDescription(field)
            # print r

    with open("Result/settlement_field_descriptions/tables/"+base, "w") as file:
            file.write(str(soup))


path_to_str="Data/settlement/tables/cfg_billing_id.html"

writeToHTML(path_to_str)
