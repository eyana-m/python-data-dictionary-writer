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

        with open("Result/settlement/tables/"+base, "w") as file:
            file.write(str(soup))

    print "Done writing field descriptions for %s"%(base)


def isCompleteDescription(basename):
    with open("Result/settlement_csv/"+basename+".csv", "rb") as f:
        reader = csv.reader(f,delimiter="|")
        header = next(reader, None)

        for row in reader:
            if row[1] in (None, ""):
                continue
            else:
                return True
        return False
        


print "------------------------------------------------------"
print "Write Field Descriptions to SchemaSpy Data Dictionary"
print "------------------------------------------------------"



source = "Result/settlement_table_desc/tables/"

pathlist = Path(source).glob('**/*.html')
count = 0;
total = 0;
for path in pathlist:

    path_in_str = str(path)
    base=os.path.basename(path_in_str)
    basename = os.path.splitext(base)[0]


    if  isCompleteDescription(basename) == True:
        writeToHTML(path_in_str)
        count = count + 1
    else:
        continue

    total = total + 1






print "---------------------------------------------------"
print "Job completed for %i out of %i tables. Check results folder." %(count, total)
print "---------------------------------------------------"
