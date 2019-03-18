import bs4

with open("ejemplo.html") as fp:
    soup = bs4.BeautifulSoup(fp, features="html.parser")

soup.prettify()

print(soup.title.string)