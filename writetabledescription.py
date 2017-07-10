import os
import csv
from bs4 import BeautifulSoup

def openCSV(table):
    with open("../../Google Drive/Python/CSV_dump/Settlement-Tables-Descriptions.csv", "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == table:
                return row[1]
                break;
print "--------------------------------------------"
print "Writing to SchemaSpy Data Dictionary..."
print "--------------------------------------------"

base=os.path.basename("Data/settlement/tables/cfg_billing_id.html")

with open("Data/settlement/tables/"+base) as inf:
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

print(tables[5])

data_table.insert_before(extraSoup)

print soup

with open("Result/settlement/tables/"+base, "w") as file:
    file.write(str(soup))
