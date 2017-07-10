import os
from bs4 import BeautifulSoup

# create new link
#new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
#soup.head.append(new_link)

#new_tag = soup.new_tag('div', id='description')
#soup.body.append(new_tag)
#print(soup.title)

base=os.path.basename("Data/settlement/tables/cfg_billing_id.html")

print(base)

with open("Data/settlement/tables/"+base) as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt, 'html.parser')

table_description_text = """
<!---Table Description--->
<br> <div><strong>Description: </strong> {Insert description here from csv source}</div> <br></br>
<!---Table Description--->"""

extraSoup = BeautifulSoup(table_description_text, 'html.parser')


head_tag = soup.head

tables = soup.find_all('table')
data_table = tables[5]

print(tables[5])

data_table.insert_before(extraSoup)

print soup

with open("Result/settlement/tables/"+base, "w") as file:
    file.write(str(soup))
