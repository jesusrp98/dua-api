import bs4

with open("ejemplo.html") as fp:
    soup = bs4.BeautifulSoup(fp, features="html.parser")


# nombre de grados
for link in soup.find_all(title='Pincha para más info sobre esta titulación'):
    print(link.string)