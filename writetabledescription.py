import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

def openCSV(table):
    with open("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == table:
                return row[1]
                break;


def writeToHTML(path):
    base=os.path.basename(path)
    with open(path) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    description = openCSV(os.path.splitext(base)[0])

    table_description_text = """
    <!---Table Description--->
    <br> <div><strong>Description: </strong> %s </div> <br></br>
    <!---Table Description--->""" % (description)

    extraSoup = BeautifulSoup(table_description_text, 'html.parser')

    head_tag = soup.head
    tables = soup.find_all('table')
    data_table = tables[5]
    data_table.insert_before(extraSoup)

    with open("Result/settlement/tables/"+base, "w") as file:
        file.write(str(soup))

    print "Done writing to %s..." % (base)


print "-----------------------------------------------------------"
print "Writing Table Descriptions to SchemaSpy Data Dictionary..."
print "-----------------------------------------------------------"

source = "Data/settlement/tables"

pathlist = Path(source).glob('**/*.html')
for path in pathlist:
    path_in_str = str(path)
    writeToHTML(path_in_str)

print "---------------------------------------------------------------"
print "Completed job for all tables. Check results folder."
print "---------------------------------------------------------------"
