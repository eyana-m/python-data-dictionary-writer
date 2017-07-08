##First Commit

from bs4 import BeautifulSoup

# create new link
#new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
# insert it into the document
#soup.head.append(new_link)

#new_tag = soup.new_tag('div', id='description')
#soup.body.append(new_tag)
#print(soup.title)

with open("tables/cfg_billing_id.html") as inf:
    txt = inf.read()
    soup = BeautifulSoup(txt, 'html.parser')

###print(soup.find_all('table'))

print(soup.name)
