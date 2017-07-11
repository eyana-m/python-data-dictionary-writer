import os
import csv
from bs4 import BeautifulSoup
from pathlib import Path

def getDescription(field,basename):
    with open("Result/settlement_csv/"+basename+".csv", "rb") as f:
        reader = csv.reader(f,delimiter="|")
        for row in reader:
            if row[0]==field:
                return row[1]


def writeToHTML(path):
    base=os.path.basename(path)
    basename = os.path.splitext(base)[0]
    with open(path) as inf:
        txt = inf.read()
        soup = BeautifulSoup(txt, 'html.parser')

    #Auto-open comments-section
    inputs = soup.find_all('input', {"id": "showComments"})
    inputs[0]['checked'] = "true"

    tables = soup.find_all('table')
    data_table = tables[5]
    table = data_table.find('tbody')
    rows = table.find_all('tr')


    for row in rows:
        field = row.contents[1].string
        description = getDescription(field,basename)
        comment_section = row.find_all("td", class_="comment detail")
        for r in comment_section:
             r.string = description

        with open("Result/settlement_field_descriptions/tables/"+base, "w") as file:
            file.write(str(soup))

    print "Done writing field description for %s"%(base)


print "-----------------------------------------------------------"
print "Writing Field Descriptions to SchemaSpy Data Dictionary"
print "-----------------------------------------------------------"


#This must be changed
source = "Result/settlement/tables/"

#pathlist = Path(source).glob('**/*.html')

pathlist = ['cfg_billing_id', 'cfg_charge_id']
for path in pathlist:
    #path_in_str = str(path)
    path_in_str = source+path+".html"
    base=os.path.basename(path_in_str)
    writeToHTML(path_in_str)


print "--------------------------------------------------------------------------"
print "Wrote all field descriptions of all settlement tables. Check results folder."
print "---------------------------------------------------------------------------"
