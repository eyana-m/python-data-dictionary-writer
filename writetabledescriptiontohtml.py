import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path


def getTableDescription(table,csv_source_path):
    with open(csv_source_path,"rU") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == table:
                return row[1]
                break;


def writeToHTML(path, csv_source_path):
    base=os.path.basename(path)
    with open(path) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    description = getTableDescription(os.path.splitext(base)[0],csv_source_path)

    table_description_text = """<br><div><strong>Description: </strong> %s </div> <br></br> """ % (description)

    extraSoup = BeautifulSoup(table_description_text, 'html.parser')

    head_tag = soup.head
    tables = soup.find_all('table')
    data_table = tables[5]
    data_table.insert_before(extraSoup)

    with open("Result/settlement_table_desc/tables/"+base, "w") as file:
        file.write(str(soup))

    print "Done writing table descriptions to %s..."% (base)


def writeToIndex(csv_source_path):

    source = "Data/settlement/index.html"
    with open(source) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    tables = soup.find_all('table')
    table_list = tables[3]

    table_names = table_list.find_all('a')

    for table in table_names:
        desc = getTableDescription(table.string,csv_source_path)
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

#file_name= raw_input("Please enter file name: ")
#print "Table Description Source: %s"%(file_name)


csv_source_path = raw_input("Please enter csv_source_path: ")
print "Table Description Source: %s"%(csv_source_path)

count = 0;

for path in pathlist:
    path_in_str = str(path)
    writeToHTML(path_in_str, csv_source_path)
    count  = count + 1;

writeToIndex(csv_source_path)

print "---------------------------------------------------------------"
print "Completed job for %d tables. Check Results folder."%(count)
print "---------------------------------------------------------------"
