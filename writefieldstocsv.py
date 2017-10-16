import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

def retrieveFields(path):
    base=os.path.basename(path)
    with open(path) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    tables = soup.find_all('table')
    data_table = tables[5]

    table = data_table.find('tbody')

    rows = table.find_all('tr')

    fields = []
    for row in rows:
        fields.append(row.contents[1].string)

    return fields

def getUniqueField(field):
    with open("Result/settlement_csv/unique_fields-sow9.csv", "r") as sow9, open("Result/settlement_csv/unique_new_fields.csv", "r") as sow10: 
        reader = csv.reader(sow9,delimiter="|")
        reader2 = csv.reader(sow10,delimiter="|")
        for row in reader:
        	if row[0]==field:
        		return row[1]
        	else:
        		continue
        for row in reader2:
            if row[0]==field:
                return row[1]
            else:
                continue            
        return None


def writeToCSV(fields, base):
    basename = os.path.splitext(base)[0]
    basename_csv_file = basename+".csv"

    with open("Result/settlement_csv/"+basename_csv_file, "w") as csv_file:
        writer = csv.writer(csv_file,delimiter="|")
        writer.writerow(["Field","Description"])

        for field in fields:
            temp = getUniqueField(field) 
            if temp in (None, ""):
                writer.writerow([field, ""])              
            else:
                writer.writerow([field, temp])     

        print "Done writing fields to %s..." % (basename_csv_file)


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


print "-----------------------------------------------------------------------------"
print "Retrieve fields and common field descriptions from SchemaSpy Data Dictionary"
print "-----------------------------------------------------------------------------"

source = "Data/settlement/tables"

pathlist = Path(source).glob('**/*.html')
for path in pathlist:
    path_in_str = str(path)
    base=os.path.basename(path_in_str)
    writeToCSV(retrieveFields(path_in_str),base)

print "---------------------------------------------------------------------"
print "Retrieved all fields of all settlement tables. Check results folder."
print "--------------------------------------------------------------------"
