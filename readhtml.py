
from bs4 import BeautifulSoup

# create new link
#new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
#soup.head.append(new_link)

#new_tag = soup.new_tag('div', id='description')
#soup.body.append(new_tag)
#print(soup.title)




with open("Data/settlement/tables/cfg_billing_id.html") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt, 'html.parser')

table_description_text = """
<!---Table Description--->
<br> <div><strong>Description: </strong> {Insert description here from csv source}</div> <br></br>
<!---Table Description--->"""

extraSoup = BeautifulSoup(table_description_text, 'html.parser')
###print(soup.find_all('table'))

###print(soup.prettify())
###print(soup.find_all('a'))

head_tag = soup.head

tables = soup.find_all('table')
data_table = tables[5]

# print(soup.head.children)
# print(len(tables))
print(tables[5])

data_table.insert_before(extraSoup)

print soup

with open("Result/settlement/tables/output1.html", "w") as file:
    file.write(str(soup))

# count = 0
# for table in tables:
#     print count, ":", table, "\n"
#     count = count + 1;
