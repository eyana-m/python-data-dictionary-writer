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
    with open("Result/settlement_csv/unique_fields.csv", "r") as f: 
        reader = csv.reader(f,delimiter="|")
        for row in reader:
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
