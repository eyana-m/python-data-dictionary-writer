import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path


def getTableDescription(table,file_name):
    with open("../../Google Drive/Python/CSV_dump/"+file_name, "rU") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == table:
                return row[1]
                break;


def writeToHTML(path, file_name):
    base=os.path.basename(path)
    with open(path) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    description = getTableDescription(os.path.splitext(base)[0],file_name)

    table_description_text = """<br><div><strong>Description: </strong> %s </div> <br></br> """ % (description)

    extraSoup = BeautifulSoup(table_description_text, 'html.parser')

    head_tag = soup.head
    tables = soup.find_all('table')
    data_table = tables[5]
    data_table.insert_before(extraSoup)

    with open("Result/settlement_table_desc/tables/"+base, "w") as file:
        file.write(str(soup))

    print "Done writing table descriptions to %s..."% (base)


def writeToIndex(file_name):

    source = "Data/settlement/index.html"
    with open(source) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    tables = soup.find_all('table')
    table_list = tables[3]

    table_names = table_list.find_all('a')

    for table in table_names:
        desc = getTableDescription(table.string,file_name)
        mother_table = table.parent.parent
        comment_section = mother_table.find_all("td", class_="comment detail")
        for c in comment_section:
            c.string = desc

    with open("Result/settlement_table_desc/index.html","w") as file:
        file.write(str(soup))

    with open("Result/settlement/index.html","w") as file:
        file.write(str(soup))

    print "Done writing table description to index.html"


print "-----------------------------------------------------------"
print "Writing Table Descriptions to SchemaSpy Data Dictionary..."
print "-----------------------------------------------------------"

source = "Data/settlement/tables"

pathlist = Path(source).glob('**/*.html')

file_name= raw_input("Please enter file_name: ")
print "Table Description Source: %s"%(file_name)

count = 0;

for path in pathlist:
    path_in_str = str(path)
    writeToHTML(path_in_str, file_name)
    count  = count + 1;

writeToIndex(file_name)

print "---------------------------------------------------------------"
print "Completed job for %d tables. Check Results folder."%(count)
print "---------------------------------------------------------------"
