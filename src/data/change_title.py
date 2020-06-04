from bs4 import BeautifulSoup
filename = "./index.html"

with open(filename, "r") as fp:
    soup = BeautifulSoup(fp, "html.parser") # Or BeautifulSoup(fp, "lxml")
    soup.title.string.replaceWith("COVID19 - La Plata")

with open(filename, "wb") as file:
    file.write(soup.prettify("utf-8"))