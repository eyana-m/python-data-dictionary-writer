import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

#Variables

source = "Data/settlement/tables"

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


# List Implementation
def retrieveUniqueFields():
    pathlist = Path(source).glob('**/*.html')

    all_fields = []
    unique_fields = []
   

    for path in pathlist:
        path_in_str = str(path)
        base=os.path.basename(path_in_str)
        all_fields.extend(retrieveFields(path_in_str))


    for field in all_fields:
        if field not in unique_fields:
            unique_fields.append(field)
        else:
            continue

    return unique_fields


#Compare SOW9 and SOW10 Fields
def retrieveNewFields():

    unique_fields = retrieveUniqueFields()

    print "Unique fields retrieved"

    sow9_fields = []
    new_fields = []
    with open("Result/settlement_csv/unique_fields-sow9.csv", "r") as sow9:
        reader1 = csv.reader(sow9,delimiter="|")
        next(reader1)
        for row in reader1:
            sow9_fields.append(row[0])

        for field in unique_fields:
            if field not in sow9_fields:
                new_fields.append(field)
            else:
                continue
        return new_fields


def writeNewFieldsToCSV(new_fields):
    print new_fields
    with open("Result/settlement_csv/unique_new_fields.csv", "w") as csv_file:
        writer = csv.writer(csv_file,delimiter="|")
        writer.writerow(["Field","Description"])
        for field in new_fields:
            writer.writerow([field, ""])
        print "Done writing %d new fields in CSV"%(len(new_fields))


writeNewFieldsToCSV(retrieveNewFields())

